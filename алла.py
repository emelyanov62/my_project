import telebot
from telebot import types
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


@bot.callback_query_handler(lambda call: True)
def about_me(call):
    if call.data == 'company':
        bot.send_message(call.message.chat.id, ('Пелёнки, пледы, комплекты из муслина 🌾 📍Рязань\n'
                                           '•изделия из 2х слойного муслина\n'
                                            '•ручная работа\n'
                                           '•качество 🔝\n'
                                            '•индивидуальный подход\n'
                                           '•лимитированные коллекции, что делает вашу покупку уникальной\n'
                                           '•доставка по России\n'
                                           '•многофункциональны в применении\n'))

    butto = types.InlineKeyboardMarkup()
    catalog = types.InlineKeyboardButton(text='посмотреть пеленки', callback_data='catalog')
        #contacts = types.InlineKeyboardButton(text='контакты', callback_data='contacts')
        #menu = types.InlineKeyboardButton(text='главное меню', callback_data='menu')

    butto.add(catalog)
    user_name = call.from_user.first_name
    bot.send_message(call.message.chat.id, f'{user_name}, предлагаю ознакомится с ассортиментом',
                         reply_markup=butto)


@bot.callback_query_handler(lambda call: True)
def about(call):
    if call.data == 'catalog':
        bot.send_message(call.message.chat.id, ('Пелёнки, пледы, комплекты из муслина 🌾 📍Рязань\n'
                                                '•изделия из 2х слойного муслина\n'
                                                '•ручная работа\n'
                                                '•качество 🔝\n'
                                                '•индивидуальный подход\n'
                                                '•лимитированные коллекции, что делает вашу покупку уникальной\n'
                                                '•доставка по России\n'
                                                '•многофункциональны в применении\n'))
        #with open('C:\\Users\\User\\Desktop\\photo.jpg', 'rb') as photo:
         #   bot.send_photo(call.message.chat.id, photo)



bot.infinity_polling()