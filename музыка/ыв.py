import requests
from bs4 import BeautifulSoup
import telebot

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36'}
name = input(':')
url = f'https://www.last.fm/search/tracks?q={name}'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')  # обрабатываем данные
data = soup.find('tr', class_='chartlist-row chartlist-row--with-artist chartlist-row--with-buylinks js-focus-controls-container')


na = data.find('td', class_='chartlist-name').text.strip()
art = data.find('td', class_='chartlist-artist').text.strip()
img = data.find('img').get('src')
time = data.find('td', class_='chartlist-duration').text.strip()
aa = data.find('td', class_='chartlist-play')
youtube_link = aa.find('a', {'data-analytics-action': 'PlayTrackOnPage'})
song_url = youtube_link.get('href')
print(art, '-', na)
print(song_url)
print(img + '\n' + time)
print()
