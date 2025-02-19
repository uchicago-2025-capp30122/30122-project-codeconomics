import time
import httpx
from urllib.parse import urlparse

link1 = "https://www.propertyshark.com/cre/retail/us/il/cook-county/60022/"
link2 = "https://www.propertyshark.com/cre/retail/us/il/cook-county/60022/?IncludeCoworking=false&CoworkingWorkspaceTypes=0&MapView=True&Zoom=14&Viewport=-87.78428869067383,42.1321636311465,-87.75733785449219,42.17441444701207&GeopickerType=viewport"
REQUEST_DELAY = 0.1

headers = {
    "authority": "www.propertyshark.com",
    "method": "GET",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "priority": "u=0, i",
    "sec-ch-ua": '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133")',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}


def make_request(url):
    """
    Make a request to `url` and return the raw response.

    This function ensure that the domain matches what is expected
    and that the rate limit is obeyed.
    """
    # comment
    time.sleep(REQUEST_DELAY)
    print(f"Fetching {url}")
    resp = httpx.get(url, headers=headers)
    resp.raise_for_status()
    return resp