from .utils import ZIP_CODES
import pathlib as Path
import csv
import os

def get_chicago_by_zipcode(path):
    """
    Import csv that still contains data from outside Chicago Zipcodes
    Return:
    a list of dictionaries of zipcode and its income
    """
    try:
        path = Path(script_dir = os.path.dirname(__file__)).parent / 'data/median_income.csv'
    except Exception:
        print('use user input')
        
    list_to_return = []
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if str(row['zip code tabulation area']) in ZIP_CODES:
                list_to_return.append({'zip code':row['zip code tabulation area'],
                                       'income': row['B06011_001E']})    
    return list_to_return

def get_aggregate_by_latlong(path):
    pass


        
