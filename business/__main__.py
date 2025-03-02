import os
from pathlib import Path

from .get_data.get_chi_portal import get_licenses, get_crime
from .get_data.census_api import get_census_data

from .analyze.operating_time import operating_time

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
    get_licenses()
    get_crime()
    get_census_data(API_KEY)

    # 2. Analyze data
    # 2.1 Calculate duration times
    licenses_path = Path(__file__).parent / "data/licenses_.json"
    operating_time(licenses_path, False)

    # 2.2 prepare crime and [income data]
    # TODO: run crime functions and [income]

    # 2.3 merge datasets

    # 2.4 run survival regression

    # Visualization




if __name__ == "__main__":
    main()
