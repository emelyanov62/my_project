from telebot import types
from teleYandex.star_home_decor.m_token import tokens
from teleYandex.star_home_decor.my_dishes import dishes
from teleYandex.star_home_decor.textiles import textile
from teleYandex.star_home_decor.decor_homes import home_in_decor

bot = tokens()


@bot.message_handler(commands=['start'])
def start(star):
    name = star.from_user.first_name
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    home_decor = types.KeyboardButton('Домашний декор')
    furniture = types.KeyboardButton('Мебель')
    smart_house = types.KeyboardButton('Умный дом')
    electronics = types.KeyboardButton('Электроника')
    type.add(home_decor, furniture)
    type.add(smart_house, electronics)
    bot.send_message(star.chat.id, f'Привет! {name} Добро пожаловать в мир эксклюзивных предложений от Яндекс Маркета, '
                                   f'Здесь ты найдешь всё необходимое для ремонта дома, стильной мебели, '
                                   f'умных решений для домашнего комфорта и электроники, которая сделает твой '
                                   f'дом уютным и современным.🪑🏠🔌Наши уникальные скидки и акции сделают твои '
                                   f'покупки не только приятными, но и выгодными.✨🛒', reply_markup=type)
    bot.send_message(star.chat.id, f'Выберите нужную категорию')


@bot.message_handler(func=lambda message: message.text == 'Главное меню')
def return_to_main_menu(message):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    home_decor = types.KeyboardButton('Домашний декор')
    furniture = types.KeyboardButton('Мебель')
    smart_house = types.KeyboardButton('Умный дом')
    electronics = types.KeyboardButton('Электроника')
    type.add(home_decor, furniture)
    type.add(smart_house, electronics)
    bot.send_message(message.chat.id, f'Выберите нужную категорию', reply_markup=type)


@bot.message_handler(func=lambda star: star.text == 'Домашний декор')
def home_decor(decor):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dishes = types.KeyboardButton('Посуда')
    textile = types.KeyboardButton('Текстиль')
    decor_home = types.KeyboardButton('Декор для дома')
    menu = types.KeyboardButton('Главное меню')
    type.add(dishes, textile)
    type.add(decor_home, menu)
    bot.send_message(decor.chat.id, f'Вы нахидитесь в категории '
                                    f'Домашний декор, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)


@bot.message_handler(func=lambda categ: categ.text == 'Посуда')
def dishes_statr(message):
    dishes(message)


@bot.message_handler(func=lambda categ: categ.text == 'Текстиль')
def textile_start(message):
    textile(message)


@bot.message_handler(func=lambda categ: categ.text == 'Декор для дома')
def home_decor_start(message):
    home_in_decor(message)


@bot.message_handler(func=lambda star: star.text == 'Мебель')
def furniture(furnitur):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    Living_room = types.KeyboardButton('Гостиная')
    textile = types.KeyboardButton('Кухня')
    menu = types.KeyboardButton('Главное меню')
    type.add(dishes, textile)
    type.add(menu)
    bot.send_message(furnitur.chat.id, f'Вы нахидитесь в категории '
                                    f'Мебель, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)



@bot.message_handler(func=lambda star: star.text == 'Умный дом')
def smart_house(smart_hous):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dishes = types.KeyboardButton('Посуда')
    textile = types.KeyboardButton('Текстиль')
    decor_home = types.KeyboardButton('Декор для дома')
    menu = types.KeyboardButton('Главное меню')
    type.add(dishes, textile)
    type.add(decor_home, menu)
    bot.send_message(smart_hous.chat.id, f'Вы нахидитесь в категории '
                                    f'Умный дом, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)



@bot.message_handler(func=lambda star: star.text == 'Электроника')
def electronics(electronic):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dishes = types.KeyboardButton('Посуда')
    textile = types.KeyboardButton('Текстиль')
    decor_home = types.KeyboardButton('Декор для дома')
    menu = types.KeyboardButton('Главное меню')
    type.add(dishes, textile)
    type.add(decor_home, menu)
    bot.send_message(electronic.chat.id, f'Вы нахидитесь в категории '
                                    f'Электроника, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)

bot.polling(none_stop=True)
