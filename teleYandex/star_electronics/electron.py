from telebot import types
import openpyxl
import os
from teleYandex.m_token import tokens
import requests

bot = tokens()
photo_path = 'C:\\Users\\User\\Desktop\\downloaded_phot.jpg'


def download_photo(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(photo_path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False


@bot.message_handler(func=lambda categ: categ.text == 'Электроника')
def electroni(electro):  #Электроника
    global photo, description, urls
    wb = openpyxl.load_workbook('C:\\Users\\User\\Desktop\\mebel.xlsx')
    shee = wb.active
    skip_first_row = True
    for row in shee.iter_rows(values_only=True):
        if skip_first_row:
            skip_first_row = False
            continue
    description, photo, urls = row[:3]
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu = types.KeyboardButton('Главное меню')
    type.add(menu)
    if download_photo(photo):
        with open(photo_path, 'rb') as photo:
            return bot.send_photo(electro.chat.id, photo, caption=f'{description}\n\n{urls}', reply_markup=type)

    os.remove(photo_path)
