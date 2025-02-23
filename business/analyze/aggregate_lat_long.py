import pathlib
import json
import csv
from shapely.geometry import Point, Polygon
from shapely.wkt import loads

path_data = pathlib.Path(__file__).parent.parent / 'data'

def basic_spatial_join():
    """
    Loads boundaries.csv and crime.json, then return the aggregate crime
    event happening per zipcodes
    Return:
    (dict) keys: zipcode, value: total crime
    """

    crimes = load_crime()
    zipcodes = load_zipcodes()

    crime_dict = dict.fromkeys([zc[0] for zc in zipcodes],0)

    for crime in crimes:
        crime_point = crime[1]
        for zc in zipcodes:
            # Only grab the tract that contains the point
            if zc[1].contains(crime_point):
                crime_dict[zc[0]] += 1

    return crime_dict

def load_crime():
    """
    load crime.json and return a list of (data, Point)
    """
    list_crime = []
    
    with open(path_data / 'crime.json', 'r') as file:
        data = json.load(file)
        for crime in data:
            if crime.get('longitude','empty') != 'empty':
                long, lat = crime['longitude'], crime['latitude']
                list_crime.append((crime['date'], Point(long, lat)))
    
    return list_crime

def load_zipcodes():
    """
    load boundaries.csv and return a list of (zip code, Polygon)
    """

    list_zipcode = []

    with open(path_data / 'boundaries.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            list_zipcode.append((row['ZIP'], loads(row['the_geom'])))

    return list_zipcode
    


        
