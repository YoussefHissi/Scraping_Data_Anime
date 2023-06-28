
import requests
from bs4 import BeautifulSoup
import json

# URL of the website to scrape
url = 'https://zoro.to/detective-conan-movie-the-story-of-haibara-ai-black-iron-mystery-train-18412'

# Send a GET request to the website
response = requests.get(url)

# Create BeautifulSoup object from the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the elements you want to scrape
# Here's an example of scraping the titles of all <h1> tags on the page
description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)

    

description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)

    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)

    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)
    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)

    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)

    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)
    
    description_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in description_div:
    description = element.text.strip()
    print(description)





