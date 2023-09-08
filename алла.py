import telebot
from telebot import types
import os
import webbrowser

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
        media_group = [types.InputMediaPhoto(open(os.path.join(photo_folder, photo_file), 'rb')) for photo_file in
                       photo_files]

        # Отправляем альбом фотографий
        bot.send_media_group(message.message.chat.id, media_group)

        but = types.ReplyKeyboardMarkup(resize_keyboard=True)
        prise = types.KeyboardButton(text = 'prise')
        web = types.KeyboardButton(text = 'связь с продавцом')
        social_network = types.KeyboardButton(text = 'social_network')
        but.add(prise, web)
        but.add(social_network)

        user_name = message.from_user.first_name
        bot.send_message(message.message.chat.id, f'{user_name}, узнайте цены, или свяжитесь с продавцом',
                         reply_markup=but)
        bot.send_message(message.message.chat.id, 'а так же подписывайтесь на соц.сети',
                         reply_markup=but)

@bot.message_handler(func=lambda message: message.text == 'social_network')
def send_price(message):
    webbrowser.open('https://vk.com/tm__touch_moments')

@bot.message_handler(func=lambda message: message.text == 'prise')
def send_price(message):
    webbrowser.open('https://vk.com/market-211836276?screen=group')


bot.infinity_polling()
