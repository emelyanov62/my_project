import telebot
import requests
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.0.0 Safari/537.36'}
query = input(': ')
url = f'https://wwv.zvuch.com/artists/{query}'
recponse = requests.get(url, headers=headers)
soup = BeautifulSoup(recponse.text, 'lxml')
data = soup.find('ul', class_='mainSongs unstyled songs songsListen favoriteConf ajaxContent')

art = data.find_all('li', class_='play')
for count in art:
    link = count.get('data-url')

    print(link)

