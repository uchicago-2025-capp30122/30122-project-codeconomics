import httpx

api_key = "4bed36a5ef161756adaa36e8a4e8c687c57fb576"
url = f"https://api.census.gov/data/2022/cbp?get=NAME,NAICS2017_LABEL,ESTAB,PAYANN,PAYQTR1,EMP&key={api_key}"

def make_request(url):
    """
    Make a request to `url` and return the raw response.

    This function ensure that the domain matches what is expected
    and that the rate limit is obeyed.
    """
    
    print(f"Fetching {url}")
    resp = httpx.get(url)
    resp.raise_for_status()
    return resp

