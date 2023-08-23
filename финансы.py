import telebot
from telebot import types
import openpyxl

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

wb = openpyxl.load_workbook('C:\\Users\\User\\Desktop\\money.xlsx')
sheet = wb.active

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот для учета расходов.")

@bot.message_handler(commands=['статистика'])
def get_statistics(message):
    expenses = list(sheet.values)

    total = sum(int(row[0]) for row in expenses[1:])
    bot.reply_to(message, f'Общая сумма: {total} руб')

@bot.message_handler(content_types=['text'])
def add_expense(message):
    expense = message.text.split()
    sheet.append(expense)
    wb.save('C:\\Users\\User\\Desktop\\money.xlsx')
    bot.reply_to(message, 'Расход добавлен в таблицу')

bot.polling()