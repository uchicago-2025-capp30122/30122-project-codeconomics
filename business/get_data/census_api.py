import httpx
import csv
from .utils import ZIP_CODES

url = 'https://api.census.gov/data/2023/acs/acs5?get=B06011_001E&for=zip%20code%20tabulation%20area:*&key='    

def get_census_data(api_key):
    """
   This function will write csv from data in census website. The data is 
   median income by zip codes across for the whole countries in 2024
    """

    census_link = f'{url}{api_key}'
    print(f"Fetching {url}")
    resp = httpx.get(census_link)
    resp.raise_for_status()

    with open('business/data/median_income.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['med_income','zip_code'])
        filtered_rows = (row for row in resp.json()[1:] if row[1] in ZIP_CODES)
        writer.writerows(filtered_rows)
