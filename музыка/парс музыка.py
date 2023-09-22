import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36'}
url = "https://muzofond.fm"
#@bot.message_handler(commands=['start'])
#def start(start):
    #responce = requests.get(url, headers=headers)
    #soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
    #data = soup.find('ul', class_='menu-box')
    #ad = data.find_all('a')
    #for counter in ad:
    #    card = counter.get('href')
    #    bot.send_message(start.chat.id, card)
    # обращаемся с определенному классу
@bot.message_handler(commands=['start'])
def start(start):
    ne = 'https://muzofond.fm/collections/new/%D0%' \
         'BD%D0%BE%D0%B2%D0%B8%D0%BD%D0%BA%D0%B8%20%D0%' \
         'B8%20%D1%85%D0%B8%D1%82%D1%8B%20%D0%BD%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8'
    responc = requests.get(ne, headers=headers)
    soup = BeautifulSoup(responc.text, 'lxml')
    data = soup.find('li', class_='play')['data-url']
    bot.send_message(start.chat.id, data)

bot.infinity_polling()
