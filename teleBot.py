import telebot
import webbrowser
import openpyxl

# Создаем новую рабочую книгу для Excel
wb = openpyxl.Workbook()
# токен бота
bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

# Выбираем активный лист (первый лист по умолчанию)
sheet = wb.active
sheet.title = "Финансы"

# Заголовки таблицы
sheet['A1'] = "Дата"
sheet['B1'] = "Описание"
sheet['C1'] = "Доходы"
sheet['D1'] = "Расходы"


# старт бота
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}, давай запишим твой бюджет ')


# доходы
@bot.message_handler(commands=['income'])
def income(message):
    bot.send_message(message.chat.id, ('введи доход'))


# расходы
@bot.message_handler(commands=['expense'])
def expense(message):
    bot.send_message(message.chat.id, ('введи расход'))


# выход
@bot.message_handler(commands=['web'])
def web(message):
    webbrowser.open('https://www.youtube.com')


bot.infinity_polling()

