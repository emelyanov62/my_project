import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                  ' AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/116.0.0.0 Safari/537.36'}
url = "https://muzofond.fm"
@bot.message_handler(commands=['start'])
def start(start):
    responce = requests.get(url, headers=headers)
    soup = BeautifulSoup(responce.text, 'lxml')  # обрабатываем данные
    data = soup.find('div', class_='burger_menu boxShadow')
    ad = data.find_all('a')
    for count in ad:

        bot.send_message(start.chat.id, count)
    # обращаемся с определенному классу

        print(ad)

bot.infinity_polling()
