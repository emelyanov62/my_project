import telebot
from telebot import types

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

@bot.message_handler(commands=['start'])
def start(message):
    button = types.InlineKeyboardMarkup()
    company = types.InlineKeyboardButton(text='Узнать о компании подробнее', callback_data='company')

    button.add(company)
    user_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'Привет, {user_name}, меня зовут Алла, я владею брендом T&M_touch moments',
                     reply_markup=button)

@bot.callback_query_handler(lambda message: True)
def handle_callback(query):
    if query.data == 'company':
        button = types.InlineKeyboardMarkup()
        catalog = types.InlineKeyboardButton(text='Посмотреть ассортимент', callback_data='catalog')

        button.add(catalog)
        user_name = query.from_user.first_name
        bot.send_message(query.message.chat.id, f'Привет, {user_name}, T&M_touch moments', reply_markup=button)
    elif query.data == 'catalog':
        butt = types.InlineKeyboardMarkup()
        catalog = types.InlineKeyboardButton(text='узнать о компании подробней', callback_data='catalog')  # обо мне

        butt.add(catalog)
        user_name = query.from_user.first_name
        bot.send_message(query.message.chat.id, f'Привет {user_name}, moments',
                         reply_markup=butt)
        pass

if __name__ == "__main__":
    bot.polling(none_stop=True)
