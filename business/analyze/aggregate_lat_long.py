import pathlib
import json
import csv
import pandas as pd
from shapely.geometry import Point
from shapely.wkt import loads

path_data = pathlib.Path(__file__).parent.parent / 'data'

def aggregate_by_zipcode():
    """
    Load the list of dictionaries of all crime events with its zipcode
    then create an aggregate count by zipcode by of total event and total only
    for theft type crime, in the form of csv
    """
    df = pd.DataFrame(get_zipcode_from_point())
    crime_counts = df.groupby('zip_code').size().reset_index(name='total_crime')
    theft_counts = df[df['crime_type'] == 'THEFT'].groupby('zip_code').size().reset_index(name='total_theft')
    result = crime_counts.merge(theft_counts, on='zip_code', how='left').fillna(0)
    result.to_csv(path_data / 'crime.csv', index=False)


def get_zipcode_from_point():
    """
    Loads boundaries.csv and crime.json, then return the list of dictionaries 
    of crime case with zipcode identifier!
    """

    crimes = load_crime()
    zipcodes = load_zipcodes()

    for crime in crimes:
        for zip_code, poly in zipcodes:
            if poly.contains(crime['point']):
                crime['zip_code'] = zip_code
    
    return crimes

def load_crime():
    """
    load crime.json and return a list of (data, Point)
    """
    list_crime = []
    
    with open(path_data / 'crime_.json', 'r') as file:
        data = json.load(file)
        for crime in data:
            long_exist = crime.get('longitude','empty') != 'empty'
            year_2024 = crime.get('date','empty')[0:4] == '2024'
            if long_exist and year_2024:
                long, lat = crime['longitude'], crime['latitude']
                list_crime.append({'crime_type':crime['primary_type'],
                                   'point':Point(long, lat)})    
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
    


        
