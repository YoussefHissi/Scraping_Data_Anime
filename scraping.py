import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
for page in range(1, 27):
    url = f'https://zoro.to/movie?page={page}'

    # Send a GET request to the website
    response = requests.get(url)

    # Create BeautifulSoup object from the response content
    soup = BeautifulSoup(response.content, 'html.parser')

    films = soup.find_all('a', {'class': 'item-qtip'})
    list_Urls = []

    for film in films:
        links = 'https://zoro.to/' + film['href']
        list_Urls.append(links)

    for url in list_Urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        overview_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div.item.item-title.w-hide > div')
        overview = overview_div[0].text.strip() if overview_div else ''

        title_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-detail > h2')
        title = title_div[0].text.strip() if title_div else ''

        aired_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(3) > span.name')
        aired = aired_div[0].text.strip() if aired_div else ''

        permited_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(4) > span.name')
        permited = permited_div[0].text.strip() if permited_div else ''

        duration_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(5) > span.name')
        duration = duration_div[0].text.strip() if duration_div else ''

        score_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(7) > span.name')
        score = score_div[0].text.strip() if score_div else ''

        studios_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-info-wrap > div.anisc-info > div:nth-child(9) > a')
        studios = studios_div[0].text.strip() if studios_div else ''

        image_div = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-poster > div > img')
        image = image_div[0]['src'] if image_div else ''

        film_direction = soup.select('#ani_detail > div > div > div.anis-content > div.anisc-detail > div.film-buttons > a')
        to_the_film='https://zoro.to'+film_direction[0]['href']
        response = requests.get(to_the_film)
        soup = BeautifulSoup(response.content, 'html.parser')
        video= soup.select('#iframe-embed')
        print(video)