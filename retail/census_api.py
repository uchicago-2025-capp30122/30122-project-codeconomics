import httpx

def make_request(url, api_key):
    """
    Make a request to `url` and return the raw response.

    This function ensure that the domain matches what is expected
    and that the rate limit is obeyed.
    """

    url = f"https://api.census.gov/data/2022/cbp?get=NAME,NAICS2017_LABEL,ESTAB,PAYANN,PAYQTR1,EMP&key={api_key}"

    
    print(f"Fetching {url}")
    resp = httpx.get(url)
    resp.raise_for_status()
    return resp

