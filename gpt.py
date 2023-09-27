import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')


@bot.message_handler(commands=['start'])
def start(mes):
    bot.send_message(mes.chat.id,
                 "Привет! Я музыкальный бот. Отправь мне название исполнителя или трека")

@bot.message_handler(func=lambda message: True)
def find_music_info(start):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/116.0.0.0 Safari/537.36'}
    query = start.text
    url = f'https://wwv.zvuch.com/artists/{query}'
    recponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(recponse.text, 'lxml')
    data = soup.find('ul', class_='mainSongs unstyled songs songsListen favoriteConf ajaxContent')
    art = data.find_all('li', class_='play')
    for count in art:
        link = count.get('data-url')
        response = requests.get(link)
        bot.send_audio(start.chat.id, audio=response.content)
bot.infinity_polling()