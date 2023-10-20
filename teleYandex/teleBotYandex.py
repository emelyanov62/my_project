from telebot import types
from teleYandex.m_token import tokens
from teleYandex.star_home_decor.my_dishes import dishes  #Посуда
from teleYandex.star_home_decor.textiles import textile  #Текстиль
from teleYandex.star_home_decor.decor_homes import home_in_decor #Декор для дома
from teleYandex.star_furniture.bedroom_star import bedrooms   #спальня
from teleYandex.star_furniture.Living_rooms import living_rooms  #гостиная
from teleYandex.star_furniture.kitchen_star import kitchens  #кухня
from teleYandex.star_smart_house.smarts_houser import home_decor_star  #Умный дом
from teleYandex.star_electronics.electron import electroni



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
    living_room = types.KeyboardButton('Гостиная')
    kitchen = types.KeyboardButton('Кухня')
    bedroom = types.KeyboardButton('Спальня')
    menu = types.KeyboardButton('Главное меню')
    type.add(living_room, kitchen)
    type.add(bedroom, menu)
    bot.send_message(furnitur.chat.id, f'Вы нахидитесь в категории '
                                    f'Мебель, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)


@bot.message_handler(func=lambda categ: categ.text == 'Спальня')
def bedrooms_start(message):
    bedrooms(message)


@bot.message_handler(func=lambda categ: categ.text == 'Гостиная')
def living_room_start(message):
    living_rooms(message)

@bot.message_handler(func=lambda categ: categ.text == 'Кухня')
def kitchens_start(message):
    kitchens(message)


@bot.message_handler(func=lambda categ: categ.text == 'Умный дом')
def smart_house_start(message):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Главное меню')
    type.add(menu)
    bot.send_message(message.chat.id, f'Вы нахидитесь в категории Умный дом', reply_markup=type)
    home_decor_star(message)


@bot.message_handler(func=lambda categ: categ.text == 'Электроника')
def electronic_start(message):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Главное меню')
    type.add(menu)
    bot.send_message(message.chat.id, f'Вы нахидитесь в категории Электроника', reply_markup=type)
    electroni(message)


bot.polling(none_stop=True)
