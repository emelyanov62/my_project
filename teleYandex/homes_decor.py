from telebot import types
from main import bot, download_photo, photo_path
import openpyxl
import os


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
