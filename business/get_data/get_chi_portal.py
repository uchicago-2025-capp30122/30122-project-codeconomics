import csv
import json
import httpx
from pathlib import Path
from .utils import ZIP_CODES

START_URL_LICENSES = "https://data.cityofchicago.org/resource/r5kz-chrr.json"
START_URL_CRIME = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
LIMIT = 1000
DEFAULT_ARGS = {"$limit": LIMIT, "$order": "id", "$offset": 0}

class RequestException(Exception):
    """
    Turn a httpx.Response into an exception.
    """
    def __init__(self, response: httpx.Response):
        super().__init__(
            f"{response.status_code} retrieving {response.url}: {response.text}"
        )



def get_request_chicago(start_url, params):
    """
    Makes an API reuqest from the Chicago Data Portal
    """
    # prepare URL to make request
    query_url = httpx.URL(start_url)
    query_url = str(query_url.copy_with(params=params))

    # make request
    response = httpx.get(query_url, follow_redirects=True)

    # Return response text if the request was sucesful

    if response.status_code == 200:
        # TODO: cacheget directory for not duplicating requests
        return response.text
    else:
        raise RequestException(response)


def get_licenses(output_filename, licenses_url=START_URL_LICENSES, params = DEFAULT_ARGS):
    # TODO: PAGINATION OF LICENSES BY ZIP CODE

    # make query for actual hearing data with links from 1st query
    licenses_data = json.loads(get_request_chicago(licenses_url, params))
    
    # TODO: r.extent with pagination
    
    # write in json format
    with output_filename.open(mode="w") as json_file:
        json.dump(licenses_data, json_file, indent=4)

def get_crime(output_filename, crime_url=START_URL_CRIME, params = DEFAULT_ARGS):
    # TODO: PAGINATION OF CRIME BY DISTRICTS/AREA/YEAR

    # make query for actual hearing data with links from 1st query
    crime_data = json.loads(get_request_chicago(crime_url, params))
    
    # TODO: r.extent with pagination
    
    # write in json format
    with output_filename.open(mode="w") as json_file:
        json.dump(crime_data, json_file, indent=4)