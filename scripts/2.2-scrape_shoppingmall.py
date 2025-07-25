# This file will scrape all shopping mall location from the website: australia-shoppings.com

import re
import csv
import requests
from bs4 import BeautifulSoup
# begin code
print("Start scraping shopping malls' coordinates.")
session = requests.Session()
URL = 'https://www.australia-shoppings.com/malls-centres/victoria'
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"
session.headers.update({"User-Agent": USER_AGENT})
request = session.get(URL, timeout=10)

# Find <ul> elements with class name 'malls-list' from HTML using BeautifulSoup
bs_object = BeautifulSoup(request.text, "lxml")
title = bs_object.find('ul', class_='malls-list')

# check if the malls' information exist and the page is valid, scrape the data
if title and request.status_code == 200:
    # find all <li> elements within the <ul>, and create a list to store coordinates
    coordinates_list = []
    content = title.find_all('li')

    # find and store the coordinates for the shopping mall
    for item in content:
        # search locations using regular expressions
        find_coordinates = re.search(r'GPS:\s(-?\d+\.\d+),\s(-?\d+\.\d+)', item.text)
        if find_coordinates:
            # extract the values of latitude and longitude and combines them into a string containing two values
            latitude = find_coordinates.group(1)
            longitude = find_coordinates.group(2)
            coordinates = f'[{latitude}, {longitude}]'
            coordinates_list.append(coordinates)

    # save malls' coordinates in the CSV file
    with open('data/landing/external_data/mall_coordinates.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['coordinates'])
        csv_writer.writerows([[coord] for coord in coordinates_list])

    print("Finished, and save in CSV.")
