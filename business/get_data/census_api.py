import httpx
import csv
import pathlib
from .utils import ZIP_CODES

url = 'https://api.census.gov/data/2023/acs/acs5?get=B06011_001E,B01003_001E&for=zip%20code%20tabulation%20area:*&key='
path_data = pathlib.Path(__file__).parent.parent / 'data' 

def get_census_data(api_key):
    """
   This function will write csv from data in census website. The data is 
   median income by zip codes across for the whole countries in 2024
    """

    census_link = f'{url}{api_key}'
    print(f"Fetching {url}")
    resp = httpx.get(census_link)
    resp.raise_for_status()

    with open(path_data / 'median_income.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['med_income','population_size','zip_code'])
        filtered_rows = (row for row in resp.json()[1:] if row[2] in ZIP_CODES)
        writer.writerows(filtered_rows)
