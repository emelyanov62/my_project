# Импортируем необходимые модули
from datetime import datetime
import openpyxl
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackQueryHandler

# Определяем состояния бота
SELECT_ACTION, ADD_INCOME, ADD_EXPENSE = range(3)

# Создаем новую рабочую книгу для Excel
wb = openpyxl.Workbook()

# Выбираем активный лист (первый лист по умолчанию)
sheet = wb.active
sheet.title = "Финансы"

# Заголовки таблицы
sheet['A1'] = "Дата"
sheet['B1'] = "Описание"
sheet['C1'] = "Доходы"
sheet['D1'] = "Расходы"

# Глобальная переменная для хранения данных о текущем действии
current_action = None

# Функция, которая будет выполнена при команде /start
def start(update, context):
    user = update.effective_user

    # Создаем клавиатуру с кнопками "Доходы" и "Расходы"
    keyboard = [
        [
            InlineKeyboardButton("Доходы", callback_data='income'),
            InlineKeyboardButton("Расходы", callback_data='expense'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Привет, {user.first_name}! Этот бот поможет тебе учитывать свои доходы и расходы в Excel таблице. Выбери действие:",
        reply_markup=reply_markup  # Отправляем клавиатуру с кнопками
    )

    # Возвращаем состояние SELECT_ACTION
    return SELECT_ACTION

# Функция для обработки выбора действия (доходы/расходы)
def select_action(update, context):
    user = update.effective_user
    query = update.callback_query

    if query.data == 'income':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Введите описание дохода, {user.first_name}:"
        )
        context.user_data['action'] = 'Доходы'
        return ADD_INCOME
    elif query.data == 'expense':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Введите описание расхода, {user.first_name}:"
        )
        context.user_data['action'] = 'Расходы'
        return ADD_EXPENSE
    else:
        return SELECT_ACTION

# Функция для обработки ввода описания дохода или расхода
def handle_description(update, context):
    user = update.effective_user
    description = update.message.text
    context.user_data['description'] = description
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Введите сумму, {user.first_name}:"
    )
    return ADD_INCOME if context.user_data['action'] == 'Доходы' else ADD_EXPENSE

# Функция для обработки ввода суммы дохода или расхода и добавление в таблицу
def handle_amount(update, context):
    user = update.effective_user
    amount = float(update.message.text)
    date = datetime.now().strftime('%Y-%m-%d')
    description = context.user_data['description']
    income = amount if context.user_data['action'] == 'Доходы' else 0
    expense = amount if context.user_data['action'] == 'Расходы' else 0

    # Добавляем данные в таблицу
    row_data = (date, description, income, expense)
    sheet.append(row_data)
    wb.save("C:\\Users\\User\\Desktop\\money.xlsx")

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f"Данные добавлены в таблицу, {user.first_name}.",
    )

    return start(update, context)

# Функция для обработки нажатий кнопок "Доходы" и "Расходы"
def button(update, context):
    query = update.callback_query
    query.answer()
    return select_action(update, context)

# Главная функция для запуска бота
def main():
    # Замените "YOUR_BOT_TOKEN" на ваш токен Telegram бота
    updater = Updater(token="6616772242:AAHtXz3fkjOtdze5mG7KxmoT6vucYZewzyw", use_context=True)
    dispatcher = updater.dispatcher

    # Обработка команд
    dispatcher.add_handler(CommandHandler("start", start))

    # Создаем конверсацию для взаимодействия с ботом
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            SELECT_ACTION: [
                CallbackQueryHandler(button),
            ],
            ADD_INCOME: [
                MessageHandler(Filters.text & ~Filters.command, handle_description),
                MessageHandler(Filters.regex('^\\d+\\.\\d{2}$'), handle_amount),
            ],
            ADD_EXPENSE: [
                MessageHandler(Filters.text & ~Filters.command, handle_description),
                MessageHandler(Filters.regex('^\\d+\\.\\d{2}$'), handle_amount),
            ],
        },
        fallbacks=[],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

