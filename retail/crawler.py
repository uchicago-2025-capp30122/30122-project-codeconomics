import sys
import json
import lxml.html
import httpx

url = 'https://www.loopnet.com/Listing/401-N-Michigan-Ave-Chicago-IL/29413982/'

def make_request(url):
    """
    Make a request to `url` and return the raw response.

    This function ensure that the domain matches what is expected
    and that the rate limit is obeyed.
    """
    
    resp = httpx.get(url)
    resp.raise_for_status()
    return resp

def scrape_park_page(url):
    """
    This function takes a URL to a park page and returns a
    dictionary with the title, address, description,
    and history of the park.

    Parameters:
        * url:  a URL to a park page

    Returns:
        A dictionary with the following keys:
            * url:          the URL of the park page
            * name:         the name of the park
            * address:      the address of the park
            * description:  the description of the park
            * history:      the history of the park
    """
    # Set up Root
    response = make_request(url)
    root = lxml.html.fromstring(response.text)
    available = root.cssselect('span.available-spaces__data-item__value-segment')

    for property in available:
        print(property.text_content())
    
    return 'done'


if __name__ == "__main__":
    """
    Tip: It can be convenient to add small entrypoints to submodules
         for ease of testing.

    In this file, we call scrape_park_page with a given URL and pretty-print
    the output.

    This allows testing that function from the command line with:

    $ python -m parks.crawler https://scrapple.fly.dev/parks/4

    Feel free to modify/change this if you wish, you won't be graded on this code.
    """
    from pprint import pprint

    if len(sys.argv) != 2:
        print("Usage: python -m parks.crawler <url>")
        sys.exit(1)
    result = scrape_park_page(sys.argv[1])
    pprint(result)
