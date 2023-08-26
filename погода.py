import telebot
from telebot import types

#токен бота
bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

# старт
@bot.message_handler(commands=['start'])
def handle_start(message):
    # Создаем клавиатуру
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаем кнопку
    item = types.KeyboardButton("Нажми меня")

    # Добавляем кнопку на клавиатуру
    markup.add(item)

    # Отправляем сообщение с клавиатурой
    bot.send_message(message.chat.id, "Привет! Я ваш телеграм-бот. Нажми кнопку:", reply_markup=markup)





bot.infinity_polling()