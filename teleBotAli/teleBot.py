from telebot import types
from my_token import tokens

bot = tokens()


# начальный экран
@bot.message_handler(commands=['start'])
def start(star):
    name = star.from_user.first_name
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mothers_and_children = types.KeyboardButton('Для мам и детей')
    home = types.KeyboardButton('Товары для дома')
    stock = types.KeyboardButton('Большие акции и скидки')
    type.add(mothers_and_children, home)
    type.add(stock)
    bot.send_message(star.chat.id, f'{name} Приветствуем тебя в мире эксклюзивных предложений на Яндекс.Маркете,'
                                   f' где мы собрали для тебя лучшие товары для мам, детей и дома! '
                                   f'🌟Здесь ты найдешь всё, что нужно для заботы о семье и создания уюта в доме.'
                                   f' Наши уникальные скидки и акции сделают твои покупки легче и более выгодными.',
                                    reply_markup=type)
    bot.send_message(star.chat.id, f'Выберите нужную категорию')


@bot.message_handler(func=lambda message: message.text == 'Главное меню')
def return_to_main_menu(message):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mothers_and_children = types.KeyboardButton('Для мам и детей')
    home = types.KeyboardButton('Товары для дома')
    stock = types.KeyboardButton('Большие акции и скидки')
    type.add(mothers_and_children, home)
    type.add(stock)
    bot.send_message(message.chat.id, f'Выберите нужную категорию', reply_markup=type)


@bot.message_handler(func=lambda star: star.text == 'Для мам и детей')
def mother_and_childre(categ):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mother = types.KeyboardButton('Посмотреть товары для мам')
    children = types.KeyboardButton('Посмотреть товары для детей')
    menu = types.KeyboardButton('Главное меню')
    type.add(mother, children)
    type.add(menu)
    bot.send_message(categ.chat.id, f'Вы нахидитесь в категории '
                                    f'Для мам и детей, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)


@bot.message_handler(func=lambda categ: categ.text == 'Посмотреть товары для мам')
def product_mother(mothers):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Посмотреть товары для детей')
    menu = types.KeyboardButton('Главное меню')
    type.add(back)
    type.add(menu)
    bot.send_message(mothers.chat.id, 'Tовары для мам', reply_markup=type)


@bot.message_handler(func=lambda categ: categ.text == 'Посмотреть товары для детей')
def product_children(children):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Посмотреть товары для мам')
    menu = types.KeyboardButton('Главное меню')
    type.add(back)
    type.add(menu)
    bot.send_message(children.chat.id, 'Tовары для детей', reply_markup=type)




@bot.message_handler(func=lambda star: star.text == 'Товары для дома')
def home(homes):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mother = types.KeyboardButton('посуда')
    children = types.KeyboardButton('декор для дома')
    children = types.KeyboardButton('хранение в доме')
    menu = types.KeyboardButton('Главное меню')
    type.add(mother, children)
    type.add(menu)
    bot.send_message(homes.chat.id, f'Вы нахидитесь в категории '
                                    f'Для мам и детей, какие товары хотите '
                                    f'посмотреть?', reply_markup=type)


@bot.message_handler(func=lambda categ: categ.text == '')
def product_mother(mothers):
    type = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Посмотреть товары для детей')
    menu = types.KeyboardButton('Главное меню')
    type.add(back)
    type.add(menu)
    bot.send_message(mothers.chat.id, 'Tовары для мам', reply_markup=type)


bot.infinity_polling()

