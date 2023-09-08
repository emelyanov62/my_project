import telebot
import time


BOT_TOKEN = '6449664194:AAGlEy8HzzRX2_dvcU_u-WJpDSLJ5gfQsWQ'

CHAT_ID = '@mmafff' # имя чата

bot = telebot.TeleBot(token=BOT_TOKEN)

def send_message(text): # функция send_message
    bot.send_message(chat_id=CHAT_ID, text=text)

while True:
    message_text = "Это ваше периодическое сообщение каждые 10 секунд."
    send_message(message_text) # вызов функции send_message
    time.sleep(10)
