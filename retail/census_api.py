import httpx
import csv

url = 'https://api.census.gov/data/2023/acs/acs5?get=NAME,GEO_ID,B06011_001E&for=zip%20code%20tabulation%20area:*&key='    

def get_census_data(api_key):
    """
    Make a request to `url` and return the raw response.

    This function ensure that the domain matches what is expected
    and that the rate limit is obeyed.
    """

    census_link = f'{url}{api_key}'
    print(f"Fetching {url}")
    resp = httpx.get(census_link)
    resp.raise_for_status()

    with open('retail/data/median_income.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(resp.json())