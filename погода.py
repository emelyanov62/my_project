import json

import telebot
import requests


#токен бота
bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')
api = ('e819478738622a4d9741e41d934f2b01')
# старт
@bot.message_handler(commands=['start'])
def start(sms):
    bot.send_message(sms.chat.id, f'привет, {sms.from_user.first_name}, напиши город')


#информация по городу
@bot.message_handler(content_types = ['text'])
def weather(sms):
    city = sms.text.strip().lower()
    info = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={city}&appid={api}&units=metric&lang=ru')
    data = json.loads(info.text)
    bot.reply_to(sms, f'сейчас погода: {data["main"]["temp"]}')





bot.infinity_polling()