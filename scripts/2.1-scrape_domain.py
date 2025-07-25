"""
This file will scrape all rental properties information from every suburbs in Victoria Australia by postcode
"""
# built-in imports
import re
from json import dump
from collections import defaultdict
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

# This function will accept the postcode and then scrape the rental property information by it.
def scrape_domain(postcode):

    # begin code
    BASE_URL = "https://www.domain.com.au"
    url_links = []
    property_metadata = defaultdict(dict)
    session = requests.Session()
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
    session.headers.update({"User-Agent": USER_AGENT})

    # visit the web for each region(postcode)
    url = BASE_URL + f"/rent/?excludedeposittaken=1&postcode={postcode}"
    request = session.get(url, timeout=10)
    bs_object = BeautifulSoup(request.text, "lxml")

    # find number of properties for the postcode, and then calculate the page number
    title = bs_object.find("h1")
    pat = re.compile("<strong>(\d+)\s")
    page_num = pat.findall(str(title))[0]
    start_page = 1
    end_page = (int(page_num) // 20) + 1
    N_PAGES = range(start_page, end_page)
    print(f"postcode:{postcode}, records start from {start_page} end to {end_page - 1}")

    # visit the webs for the region in all pages, generate list of urls to visit
    for page in N_PAGES:
        url = BASE_URL + f"/rent/?excludedeposittaken=1&postcode={postcode}&page={page}"
        print(f"Visiting {url}")
        request = session.get(url, timeout=10)

        # if the page is valid, scrape the data
        if request.status_code == 200:
            bs_object = BeautifulSoup(request.content, "lxml")
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
        else:
            print("Access Failed.")

    # for each url, scrape some basic metadata
    for property_url in url_links[1:]:
        request = session.get(property_url, timeout=10)
        bs_object = BeautifulSoup(request.content, "lxml")
        try:
            # store postcode for each properties to merge external data next
            property_metadata[property_url]['postcode'] = postcode

            # looks for the header class to get property name
            property_metadata[property_url]['name'] = bs_object \
                .find("h1", {"class": "css-164r41r"}) \
                .text

            # looks for the div containing a summary title for cost
            property_metadata[property_url]['cost_text'] = bs_object \
                .find("div", {"data-testid": "listing-details__summary-title"}) \
                .text

            # extract coordinates from the hyperlink provided
            # i'll let you figure out what this does :P /// We can rename the 'coordinates' as 'geometry'///
            property_metadata[property_url]['coordinates'] = [
                float(coord) for coord in re.findall(
                    r'destination=([-\s,\d\.]+)', # use regex101.com here if you need to
                    bs_object \
                        .find(
                            "a",
                            {"target": "_blank", 'rel': "noopener noreferrer"}
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
            continue

    print("writing to json")
    # output to example json in data/raw/
    path = f'../real-estate-industry-project-open-source-industry-project-22/data/landing/domain_data/rent_record-{postcode}.json'
    with open(path, 'w') as f:
        dump(property_metadata, f)
        
    return

# find all data for VIC according to the post code
postcode = range(3000, 4000)
for i in postcode:
    scrape_domain(i)