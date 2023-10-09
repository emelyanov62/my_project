import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36'}
#name = input(':')
url = f'https://vk.com/audios350619743?block=new_songs&section=explore'

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')  # обрабатываем данные
data = soup.find_all('div', class_='audio_page__audio_rows _audio_page__audio_rows')
#youtube_link = data.find('a', {'data-analytics-action': 'PlayTrackOnPage'})


print(data)

