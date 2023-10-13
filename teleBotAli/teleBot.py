from telebot import types
from my_token import tokens
import openpyxl
import requests
import os

bot = tokens()


# начальный экран
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


photo_path = 'C:\\Users\\User\\Desktop\\downloaded_photo.jpg'


def download_photo(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(photo_path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False


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
def dishes(dishe):
    global photo, description, urls
    wb = openpyxl.load_workbook('C:\\Users\\User\\Desktop\\aa.xlsx')
    sheet = wb.active
    skip_first_row = True
    for row in sheet.iter_rows(values_only=True):
        if skip_first_row:
            skip_first_row = False
            continue
        description, photo, urls = row[:3]
    typee = types.ReplyKeyboardMarkup(resize_keyboard=True)
    textile = types.KeyboardButton('Текстиль')
    decor_home = types.KeyboardButton('декор для дома')
    menu = types.KeyboardButton('Главное меню')
    typee.add(textile, decor_home)
    typee.add(menu)
    if download_photo(photo):
        with open(photo_path, 'rb') as photo:
            bot.send_photo(dishe.chat.id, photo, caption=f'{description}\n\n{urls}', reply_markup=typee)

    os.remove(photo_path)



bot.infinity_polling()

