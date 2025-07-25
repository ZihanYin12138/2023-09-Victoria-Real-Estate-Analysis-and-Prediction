"""
A very simple, naive, and basic web scraping script. This will not
work completely and is only applicable to domain.com.

Feel free to use this as a source of inspiration, it is by no means production code.
"""
# built-in imports
import re
from json import dump

from collections import defaultdict

# user packages
from bs4 import BeautifulSoup
from urllib.request import urlopen

# constants
BASE_URL = "https://www.domain.com.au"
N_PAGES = range(1, 10) # update this to your liking
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}
# begin code
url_links = []
property_metadata = defaultdict(dict)

# generate list of urls to visit
for page in N_PAGES:
    url = BASE_URL + f"/rent/melbourne-region-vic/?sort=price-desc&page={page}"
    print(f"Visiting {url}")
    bs_object = BeautifulSoup(urlopen(url, timeout = 20, headers = HEADERS), "lxml")

    # find the unordered list (ul) elements which are the results, then
    # find all href (a) tags that are from the base_url website.
    index_links = bs_object \
        .find(
            "ul",
            {"data-testid": "results"}
        ) \
        .findAll(
            "a",
            href=re.compile(f"{BASE_URL}/*") # the `*` denotes wildcard any
        )

    for link in index_links:
        # if its a property address, add it to the list
        if 'address' in link['class']:
            url_links.append(link['href'])

# for each url, scrape some basic metadata
for property_url in url_links[1:]:
    bs_object = BeautifulSoup(urlopen(property_url), "lxml")
    try: 
        # looks for the header class to get property name
        property_metadata[property_url]['name'] = bs_object \
            .find("h1", {"class": "css-164r41r"}) \
            .text

        # looks for the div containing a summary title for cost
        property_metadata[property_url]['cost_text'] = bs_object \
            .find("div", {"data-testid": "listing-details__summary-title"}) \
            .text

        # extract coordinates from the hyperlink provided
        # i'll let you figure out what this does :P
        property_metadata[property_url]['coordinates'] = [
            float(coord) for coord in re.findall(
                r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
                bs_object \
                    .find(
                        "a",
                        {"target": "_blank", 'rel': "noopener noreferer"}
                    ) \
                    .attrs['href']
            )[0].split(',')
        ]

        # get rooms and parking
        rooms = bs_object \
                .find("div", {"data-testid": "property-features"}) \
                .findAll("span", {"data-testid": "property-features-text-container"})

        # rooms
        property_metadata[property_url]['rooms'] = [
            re.findall(r'\d+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Bed' in feature.text or 'Bath' in feature.text
        ]
        # parking
        property_metadata[property_url]['parking'] = [
            re.findall(r'\S+\s[A-Za-z]+', feature.text)[0] for feature in rooms
            if 'Parking' in feature.text
        ]

        property_metadata[property_url]['desc'] = re \
            .sub(r'<br\/>', '\n', str(bs_object.find("p"))) \
            .strip('</p>')
    except AttributeError:
        print(f"Issue with {url}, see raw dump below")
        print(bs_object.text)
        continue

# output to example json in data/raw/
with open('../data/raw/example.json', 'w') as f:
    dump(property_metadata, f)
