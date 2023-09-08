import telegram
from bs4 import BeautifulSoup
import requests
import time

# Токен вашего бота
TOKEN = '6449664194:AAGlEy8HzzRX2_dvcU_u-WJpDSLJ5gfQsWQ'

# Идентификатор чата, куда будут отправляться новости
CHAT_ID = '6688470974'

# URL новостного сайта для скрапинга
NEWS_URL = 'https://example.com/news'

# Функция для отправки сообщений
def send_message(text):
    bot = telegram.Bot(token=TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=text)

# Функция для скрапинга новостей
def scrape_news():
    response = requests.get(NEWS_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Здесь можно добавить код для извлечения новостей из HTML-кода сайта

    # Отправка новостей в чат
    for news_item in news_list:
        send_message(news_item)

# Основной цикл бота
while True:
    scrape_news()
    time.sleep(3600)  # Проверять новости каждый час

