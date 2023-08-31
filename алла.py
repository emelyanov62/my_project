import telebot
from telebot import types
import os

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

@bot.message_handler(commands=['start'])
def start(message):
    button = types.InlineKeyboardMarkup()
    company = types.InlineKeyboardButton(text='узнать о компании подробней', callback_data='company')  # обо мне

    button.add(company)
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет {user_name}, меня зовут Алла, я владею брендом T&M_touch moments',
                     reply_markup=button)


@bot.callback_query_handler(lambda message: True)
def about_me(message):
    if message.data == 'company':
        button = types.InlineKeyboardMarkup()
        catalog = types.InlineKeyboardButton(text='посмотреть пеленки', callback_data='catalog')
        button.add(catalog)
        bot.send_message(message.message.chat.id, ('Пелёнки, пледы, комплекты из муслина 🌾 📍Рязань\n'
                                                   '•изделия из 2х слойного муслина\n'
                                                   '•ручная работа\n'
                                                   '•качество 🔝\n'
                                                   '•индивидуальный подход\n'
                                                   '•лимитированные коллекции, что делает вашу покупку уникальной\n'
                                                   '•доставка по России\n'
                                                   '•многофункциональны в применении\n'))

        user_name = message.from_user.first_name
        bot.send_message(message.message.chat.id, f'{user_name}, предлагаю ознакомится с ассортиментом',
                         reply_markup=button)

    elif message.data == 'catalog':

        photo_folder = 'C:\\Users\\User\\Desktop\\photo'

        # Получаем список файлов в папке
        photo_files = [f for f in os.listdir(photo_folder) if os.path.isfile(os.path.join(photo_folder, f))]

        # Отправляем все фотографии из папки
        for photo_file in photo_files:
            photo_path = os.path.join(photo_folder, photo_file)
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.message.chat.id, photo)

        button = types.InlineKeyboardMarkup()
        yes = types.InlineKeyboardButton(text='да', callback_data='yes')  # обо мне
        no = types.InlineKeyboardButton(text='нет', callback_data='ho')

        button.add(yes, no)
        user_name = message.from_user.first_name
        bot.send_message(message.message.chat.id, f'ну как ксю? ништяк?))',
                         reply_markup=button)


bot.infinity_polling()