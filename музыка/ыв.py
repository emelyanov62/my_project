import telebot
import requests
from bs4 import BeautifulSoup
import random

url = f'https://wwv.zvuch.com/artists/korn'
recponse = requests.get(url)
soup = BeautifulSoup(recponse.text, 'lxml')
data = soup.find('ul', class_='mainSongs unstyled songs songsListen favoriteConf ajaxContent')
art = data.find_all('li', class_='play')

sp = []
if data:
    art = data.find_all('li', class_='play')
    for count in art:
        link = count.get('data-url')
        sp.append(link)
        num = 0
        if num >= 5:
            break
        response = requests.get(link)
        bot.send_audio(start.chat.id, audio=response.content)
        num += 1

