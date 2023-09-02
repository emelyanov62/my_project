import telebot
from telebot import types  #  кнопка
import yadisk  # ссылки на диск

bot = telebot.TeleBot('6297727546:AAE65ZEpHy5Of4RYacKOiv1if8qclhXaZuk')
yandex_disk = yadisk.YaDisk(token='y0_AgAAAABZVEkRAApvDAAAAADrupX-FWQpg2UCQ1Go2XgmQGpqkQwrXoY')

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


#  ассортимент и поиск
@bot.message_handler(func=lambda message: message.text == 'пеленки')  # пеленки
def menu(message):
    folder_path = '/path/to/your/алла/'

    # Список файлов в указанной папке
    yandex_file_path = yandex_disk.listdir(folder_path)

    # Скачиваем файл с Яндекс.Диска
    with yandex_disk.download(yandex_file_path) as f:
        bot.send_photo(message.chat.id, f)



#  Корзина


bot.infinity_polling()