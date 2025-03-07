import os
from pathlib import Path
import time

from .get_data.get_chi_portal import get_licenses, get_crime
from .get_data.census_api import get_census_data
from .analyze.aggregate_lat_long import aggregate_by_zipcode
from .analyze.operating_time import operating_time
from .app import app

def main():
    # 0. make sure to have APIKEY
    try:
        API_KEY = os.environ["API_KEY"]
    except KeyError:
        raise Exception(
            "Make sure that you have set the API Key environment variable as "
            "described in the README."
        )

    # 1. Run functions to get data
    print('Getting License Data - On Going') 
    get_licenses()
    time.sleep(1)
    print('Getting Crime Data - On Going')
    get_crime()
    time.sleep(1)
    print('Getting Census Data - On Going')
    get_census_data(API_KEY)
    print('All data has been obtained!')

    # 2. Analyze data
    # 2.1 Calculate duration times and write a CSV of the results
    print('Processing Data: Get Operating Time')
    licenses_path = Path(__file__).parent / "data/licenses_.json"
    operating_time(licenses_path, False)

    # 2.2 prepare crime data
    print('Processing Data: Do Spatial Join')
    aggregate_by_zipcode()

if __name__ == "__main__":
    main()
