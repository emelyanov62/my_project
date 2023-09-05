import telebot
from telebot import types  #  кнопка
import sqlite3

bot = telebot.TeleBot('6297727546:AAE65ZEpHy5Of4RYacKOiv1if8qclhXaZuk')


#  Приветственное сообщение
@bot.message_handler(commands = ['start'])
def start(start):
    user_name = start.from_user.first_name
    user_surname = start.from_user.last_name

    start_0 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    start_1 = types.KeyboardButton('посмотреть ассортимент')
    start_0.add(start_1)
    bot.send_message(start.chat.id, f'Добро пожаловать {user_name} {user_surname},  магазин Пеленки,'
                                    f' пледы из муслина T&M_touch moments! '
                                    f'предлагает широкий ассортимент товаров для вас и вашего малыша. '
                                    f'Вы можете просматривать наши товары по категориям, использовать поиск или '
                                    f'добавить товары в корзину',
                     reply_markup=start_0)


#  Меню навигации
@bot.message_handler(func=lambda start: start.text == 'посмотреть ассортимент')
def menu(message):
    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    diaper =types.KeyboardButton('пеленки')
    blankets = types.KeyboardButton('пледы')
    bib = types.KeyboardButton('нагрудники')
    menu.add(diaper, blankets, bib)
    bot.send_message(message.chat.id, f'{user_name} {user_surname}, выберите одну из интересующей категории',
                     reply_markup=menu)


#  ассортимент
@bot.message_handler(func=lambda message: message.text == 'пеленки')  # пеленки
def menu(message):
    conn = sqlite3.connect('diaper.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE name = "пеленка"')  # Выполняем SQL-запрос для извлечения данных о пеленках
    diapers = cursor.fetchall()  # Получаем результаты запроса
    conn.close()  # Закрываем соединение

    if diapers:  # Отправляем информацию о пеленках в чат
        for diaper in diapers:
            product_id, product_name, product_description, product_price, product_quantity, product_image = diaper
            bot.send_photo(message.chat.id, product_image)  # Здесь product_image должно быть изображением в нужном формате.
            button = types.InlineKeyboardMarkup()
            catalog = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='catalog')
            button.add(catalog)
            product_id, product_name, product_description, product_price, product_quantity, product_image = diaper
            bot.send_message(message.chat.id, f"Название: {product_name}\nОписание: {product_description}\n"
                                                f"Цена: {product_price} руб.\nКоличество в наличии: {product_quantity}",
                             reply_markup=button)

    else:
        bot.send_message(message.chat.id, "Извините, товары 'пеленки' не найдены.")


user_cart = {}  # Словарь для хранения корзины пользователя. название, количество, фото.


#  Корзина
@bot.callback_query_handler(lambda message: True)
def add_to_cart(message):
    if message.data == 'catalog':
        # Здесь вы можете предоставить пользователю список товаров и попросить его выбрать товар для добавления
        # Например, путем отображения клавиатуры с вариантами товаров и их описаниями
        # После выбора пользователем товара, вы можете получить его ID и количество
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        diaper = types.KeyboardButton('корзина')
        blankets = types.KeyboardButton('пледы')
        bib = types.KeyboardButton('нагрудники')
        menu.add(diaper)
        menu.add(blankets, bib)

        product_id = 1  # ID выбранного товара (ваше значение)
        quantity = 1
        product_name = "Пеленка"

        # Добавляем товар в корзину пользователя
        if product_id in user_cart:
            user_cart[product_id]['quantity'] += quantity
        else:
            user_cart[product_id] = {
                'name': product_name,
                #'image': product_image,
                'quantity': quantity
            }

        bot.send_message(message.message.chat.id, f"Товар добавлен в корзину.",
                         reply_markup=menu)


# Обработчик для просмотра корзины
@bot.message_handler(func=lambda message: message.text == 'корзина')
def view_cart(message):
    if not user_cart:
        bot.send_message(message.chat.id, "Ваша корзина пока пуста.")
    else:
        for product_id, product_info in user_cart.items():
            name = product_info['name']
            #image = product_info['image']
            quantity = product_info['quantity']

            bot.send_message(message.chat.id, f"Название: {name}\nКоличество: {quantity}")
            #bot.send_photo(message.chat.id, image)

# Другие обработчики для удаления товаров из корзины, оформления заказа и др. можно добавить аналогично.

# Запуск бота
bot.infinity_polling()
