from telebot import types
import sqlite3
from my_token import tokens
import tempfile


bot = tokens()

# начальный экран
@bot.message_handler(commands= ['start'])
def start(star):
    name = star.from_user.first_name
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    categories = types.KeyboardButton('посмотреть категории')
    whole_range = types.KeyboardButton('посмотреть все товары')
    top = types.KeyboardButton('часто заказывают')
    stock = types.KeyboardButton('акции и скидки')
    type.add(categories, whole_range)
    type.add(top, stock)
    bot.send_message(star.chat.id, f"Привет, {name}! Здесь ты найдешь топовые товары"
                                    f" с AliExpress по разным категориям, а "
                                    f"также уникальные скидки и акции. "
                                    f"Погрузись в мир эксклюзивных предложений и"
                                    f" сделай свои покупки легче и удобнее!",
                                    reply_markup=type)


#bot.message_handler(func=lambda star: star.text == 'посмотреть категории')
#def categorie (categ):


# весь товар
@bot.message_handler(func=lambda star: star.text == 'посмотреть все товары')
def whole_rang(whole):
    types_whole_range = types.ReplyKeyboardMarkup(resize_keyboard=True)
    categories = types.KeyboardButton('посмотреть категории')
    top = types.KeyboardButton('часто заказывают')
    stock = types.KeyboardButton('акции и скидки')
    types_whole_range.add(categories)
    types_whole_range.add(top, stock)

    # Отправляем клавиатуру с вариантами действий
    bot.send_message(whole.chat.id, 'Выберите действие:', reply_markup=types_whole_range)


#@bot.message_handler(func=lambda star: star.text == 'часто заказывают')
#def top(topp):


#@bot.message_handler(func=lambda star: star.text == 'акции и скидки')
#def stok(stoc):

bot.infinity_polling()
#whole_rang(gets())
