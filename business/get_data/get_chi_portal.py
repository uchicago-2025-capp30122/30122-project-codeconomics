import json
import httpx
from pathlib import Path
from .utils import ZIP_CODES
import re

START_URL_LICENSES = "https://data.cityofchicago.org/resource/r5kz-chrr.json"
START_URL_CRIME = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"
LIMIT = 50000
DEFAULT_ARGS = {"$limit": LIMIT, "$order": "id"}
ALLOWED_CHARS = "abcdefghijklmnopqrstuvwxyz1234567890%+,^=_"
CACHE_DIR = Path(__file__).parent.parent / "data/cached"
CRIME_YEARS = ["2024", "2025"]


class RequestException(Exception):
    """
    Turn a httpx.Response into an exception.
    """

    def __init__(self, response: httpx.Response):
        super().__init__(
            f"{response.status_code} retrieving {response.url}: {response.text}"
        )


def url_to_cache_key(url: str) -> str:
    """
    Convert a URL to a cache key that can be stored on disk.

    This lets us administer unique filenames per request.
    """
    url_pivot = url.lower().removeprefix("https://")
    cache_key = re.sub(f"[^{re.escape(ALLOWED_CHARS)}]", "_", url_pivot)

    return cache_key


def get_request_chicago(start_url, params):
    """
    This function makes an API request to the Chicago Data Portal
    Inputs:
        -start_url: URL for the database to make a request
        -params: parameters of the request, include default for pagination and
                particular for the database

    Returns:
        -text of the request if it was sucessful (200)
    Raises:
        -RequestException if response was not sucessful
    """
    # prepare URL to make request
    query_url = httpx.URL(start_url)
    query_url = str(query_url.copy_with(params=params))

    # get the cache key and directory
    cache_key = url_to_cache_key(query_url)
    cached_key_path = CACHE_DIR / cache_key

    # check if request was done before
    if cached_key_path.exists():
        return cached_key_path.read_text()

    # make request if it was not done before
    response = httpx.get(query_url, follow_redirects=True)
    if response.status_code == 200:
        CACHE_DIR.mkdir(exist_ok=True, parents=True)
        cached_key_path.write_text(response.text)
        return response.text
    else:
        raise RequestException(response)


def get_licenses(licenses_url=START_URL_LICENSES, params=DEFAULT_ARGS):
    licenses_data = []
    for zip in ZIP_CODES:
        n_rows = LIMIT
        params["zip_code"] = zip
        params["$offset"] = 0

        while n_rows == LIMIT:
            licenses_request = json.loads(get_request_chicago(licenses_url, params))
            licenses_data.extend(licenses_request)

            n_rows = len(licenses_request)
            params["$offset"] = params.get("$offset") + LIMIT

    # write in json format
    output_filename = Path(__file__).parent.parent / "data/licenses_.json"
    with output_filename.open(mode="w") as json_file:
        json.dump(licenses_data, json_file, indent=4)


def get_crime(crime_url=START_URL_CRIME, params=DEFAULT_ARGS):
    crime_data = []
    for year in CRIME_YEARS:
        n_rows = LIMIT
        params["year"] = year
        params["$offset"] = 0
        params["$limit"] = LIMIT

        while n_rows == LIMIT:
            crime_request = json.loads(get_request_chicago(crime_url, params))
            crime_data.extend(crime_request)
            n_rows = len(crime_request)
            params["$offset"] = params.get("$offset") + LIMIT

    # write in json format
    output_filename = Path(__file__).parent.parent / "data/crime_.json"
    with output_filename.open(mode="w") as json_file:
        json.dump(crime_data, json_file, indent=4)
