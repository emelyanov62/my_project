import telebot
from telebot import types  # модуль кнопки

bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

# Обработка команды /start
@bot.message_handler(commands=['start']) # дикоратор который принимает команды с чата
def send_welcome(message):  # текст из чата
    # Создание клавиатуры
    keyboard = types.InlineKeyboardMarkup()  # кнопка под текстом
    yes_button = types.InlineKeyboardButton(text='да', callback_data='yes')  # текст в кнопке

    keyboard.add(yes_button) # добавляем кнопку
    bot.send_message(chat_id=update.effective_chat.id, 'салют?', reply_markup = keyboard) # текст над кнопкой


@bot.callback_query_handler(lambda call: True) # дикоратор вызываться каждый раз, когда пользователь нажимает на кнопку или выполняет другие действия
def ancwer(call): # функция обрабатывает кнопку
    if call.data == 'yes': # data это кнопка
        keyword = types.InlineKeyboardMarkup()
        item_id = types.InlineKeyboardButton(text='мой id', callback_data='yes')
        keyword.add(item_id)
        bot.send_message(call.message.chat.id, 'нажмите подтвердить',
                         reply_markup=keyword)


bot.infinity_polling()