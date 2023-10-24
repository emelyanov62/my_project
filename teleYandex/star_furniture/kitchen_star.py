from telebot import types
import openpyxl
import os
from teleYandex.m_token import tokens
import requests

bot = tokens()
photo_path = 'C:\\Users\\User\\Desktop\\downloaded_photo.jpg'


def download_photo(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open(photo_path, 'wb') as file:
            file.write(response.content)
        return True
    else:
        return False


# Загрузка данных из Excel в список
def load_data_from_excel(file_path):
    data = []
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    for row in sheet.iter_rows(values_only=True):
        description, photo, urls = row[:3]
        data.append((description, photo, urls))
    return data


data_list = load_data_from_excel('C:\\Users\\User\\Desktop\\кухня.xlsx')


@bot.message_handler(func=lambda categ: categ.text == 'Кухня')
def kitchens(kitche):  #кухня
    for description, photo, urls in data_list:
        typee = types.ReplyKeyboardMarkup(resize_keyboard=True)
        living_room = types.KeyboardButton('Гостиная')
        bedroom = types.KeyboardButton('Спальня')
        menu = types.KeyboardButton('Главное меню')
        typee.add(living_room, bedroom)
        typee.add(menu)
        if download_photo(photo):
            with open(photo_path, 'rb') as photo:
                bot.send_photo(kitche.chat.id, photo, caption=f'{description}\n\n{urls}', reply_markup=typee)
            os.remove(photo_path)
