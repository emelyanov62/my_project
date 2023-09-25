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
    url = f'https://www.last.fm/search/tracks?q={query}'
    recponse = requests.get(url, headers=headers)
    soup = BeautifulSoup(recponse.text, 'lxml')
    data = soup.find('tr', class_='chartlist-row chartlist-row--with-artist chartlist-row--with-buylinks js-focus-controls-container')
    art = data.find('td', class_='chartlist-artist').text.strip()
    aa = data.find('td', class_='chartlist-play')
    youtube_link = aa.find('a', {'data-analytics-action': 'PlayTrackOnPage'})
    song_url = youtube_link.get('href')
    bot.send_message(start.chat.id, text = song_url)


bot.infinity_polling()
