import telebot
from telebot import types

# Создание экземпляра бота
bot = telebot.TeleBot('6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw')

# Обработка команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создание клавиатуры
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создание кнопок
    date_button = types.KeyboardButton('Выбрать дату')
    price_button = types.KeyboardButton('Прайс')
    portfolio_button = types.KeyboardButton('Портфолио')
    payment_button = types.KeyboardButton('Оплата')

    # Добавление кнопок на клавиатуру
    markup.add(date_button, price_button)
    markup.add(portfolio_button)
    markup.add(payment_button)

    # Отправка сообщения с клавиатурой
    bot.reply_to(message, 'Привет! Чем я могу тебе помочь?', reply_markup=markup)

# Обработка команды "Выбрать дату"
@bot.message_handler(func=lambda message: message.text == 'Выбрать дату')
def choose_date(message):
    bot.reply_to(message, 'Пожалуйста, выберите удобную для вас дату.')

# Обработка команды "Прайс"
@bot.message_handler(func=lambda message: message.text == 'Прайс')
def send_price(message):
    bot.reply_to(message, 'Ниже приведены цены на мои услуги:\n\n- Фотосессия на улице: $100\n- Съемка мероприятия: $200\n- Студийная съемка: $150')

# Обработка команды "Портфолио"
@bot.message_handler(func=lambda message: message.text == 'Портфолио')
def send_portfolio(message):
    bot.reply_to(message, 'Моё портфолио можно посмотреть на сайте: example.com')

# Обработка команды "Оплата"
@bot.message_handler(func=lambda message: message.text == 'Оплата')
def send_payment(message):
    bot.reply_to(message, 'Пожалуйста, произведите оплату по следующим реквизитам:\n\nНомер карты: 1234 5678 9012 3456\nСумма: $100')

# Запуск бота
bot.polling()