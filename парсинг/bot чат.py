import telebot
from парсинг2 import arrey

bot = telebot.TeleBot('6449664194:AAGlEy8HzzRX2_dvcU_u-WJpDSLJ5gfQsWQ')
CHAT_ID = '@mmafff'  # имя чата


def send_messages(messages):
    for count in messages:
        message_text = f"Ссылка: {count[0]}\nНазвание: {count[1]}\nЦена: {count[2]}\nОписание: {count[3]}"  # Объединение аргументов в одну строку
        bot.send_message(chat_id=CHAT_ID, text=message_text)

send_messages(arrey())
