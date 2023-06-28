
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
overview_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
for element in overview_div:
    overview = element.text.strip()

    

title_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-detail > h2')
for element in title_div:
    title = element.text.strip()
  

aired_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(3) > span.name')
for element in aired_div:
    aired = element.text.strip()



permited_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(4) > span.name')
for element in permited_div:
    permited = element.text.strip()


duration_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(5) > span.name')
for element in duration_div:
    duration = element.text.strip()
   

    score_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(7) > span.name')
for element in score_div:
    score = element.text.strip()
    
studios_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(9) > a')
for element in studios_div:
    studios = element.text.strip()
    
   

film={
    "film":title,
    "overview":overview,
    "duration":duration,
    "score":score,
    "aired":aired,
    "permited":permited,
    "studios":studios,
}