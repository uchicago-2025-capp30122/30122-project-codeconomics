import pathlib
import json
import csv
import pandas as pd
from shapely.geometry import Point
from shapely.wkt import loads

path_data = pathlib.Path(__file__).parent.parent / 'data'

def aggregate_by_zipcode():
    """
    Load the list of crime dictionaries, then do the aggregation of total crime
    case and theft case by zip codes! Write the dataframe into .csv
    Return:
    -
    """
    df = pd.DataFrame(get_zipcode_from_point())
    # Get total of crime case
    crime_counts = df.groupby('zip_code').size()\
        .reset_index(name='total_crime')
    # Get total of theft only case
    theft_counts = df[df['crime_type'] == 'THEFT'].groupby('zip_code').size()\
        .reset_index(name='total_theft')
    # Merge both result
    result = crime_counts.merge(theft_counts, on='zip_code', how='left')\
        .fillna(0)
    result.to_csv(path_data / 'crime.csv', index=False)


def get_zipcode_from_point():
    """
    Loads two lists: list of (crime type, Point) and
    list of (zip code, Polygon). Then will grab crime cases that belong to
    Chicago's zip_codes, also adding zip_code key to crim dictionaries
    Return:
    (list) List of dicts with keys zip_code, crime_type, point
    """

    crimes = load_crime()
    zipcodes = load_zipcodes()

    for crime in crimes:
        for zip_code, poly in zipcodes:
            # Take if point falls within any polygon of Chicago's zipcodes
            if poly.contains(crime['point']):
                crime['zip_code'] = zip_code

    return crimes


def load_crime():
    """
    Load crime_.csv consisted of crime cases' details,
    then keep the crime type information and make a Point object from
    the coordinate columns as dictionaries
    Return:
    (list) List of Dicts with keys crime_type and point
    """
    list_crime = []

    with open(path_data / 'crime_.json', 'r') as file:
        data = json.load(file)
        for crime in data:
            # Some cases suffer from missing value on its Longitude Col
            long_exist = crime.get('longitude','empty') != 'empty'
            year_2024 = crime.get('date','empty')[0:4] == '2024'
            # Filter if the crime case could be located
            # and happened in 2024
            if long_exist and year_2024:
                long, lat = crime['longitude'], crime['latitude']
                list_crime.append({'crime_type':crime['primary_type'],
                                   'point':Point(long, lat)})
    return list_crime


def load_zipcodes():
    """
    Load boundaries.csv, then keep the ZIP value and make a Polygon object
    from the geometric column (Multipolygon)
    Return:
    (list) List of tuples (Zip Code, Polygon)
    """

    list_zipcode = []

    with open(path_data / 'boundaries.csv', 'r') as file:
        data = csv.DictReader(file)
        for row in data:
            # Use loads function to ensure the Multipolygon
            # stored properly
            list_zipcode.append((row['ZIP'], loads(row['the_geom'])))

    return list_zipcode




