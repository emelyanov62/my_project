import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36'}
#name = input(':')
url = f'https://www.last.fm/search/tracks?q=макс корж'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')  # обрабатываем данные
data = soup.find('tr', class_='chartlist-row chartlist-row--with-artist chartlist-row--with-buylinks js-focus-controls-container')
youtube_link = data.find('a', {'data-analytics-action': 'PlayTrackOnPage'})


song_url = youtube_link('href')
for count in song_url:
    print(song_url.text.strip())

