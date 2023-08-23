import openpyxl
from datetime import datetime

# Создаем новую рабочую книгу
wb = openpyxl.Workbook()

# Выбираем активный лист (первый лист по умолчанию)
sheet = wb.active
sheet.title = "Финансы"

# Заголовки таблицы
sheet['A1'] = "Дата"
sheet['B1'] = "Описание"
sheet['C1'] = "Доходы"
sheet['D1'] = "Расходы"
sheet['F1'] = "Доходы общ."
sheet['G1'] = "Расходы общ."

start = input('нажмите старт: ')

while start == 'старт':
    current_date = datetime.now()
    date = current_date.strftime('%Y-%m-%d')
    sheet['A1'] = date

    total_income = 0
    total_expense = 0

# Ввод данных с автоматически обновляемой датой
    while True:
        action = input("Выберите действие (доходы/расходы/выход): ").strip().lower()

        if action == 'выход':
            break

        if action not in ['доходы', 'расходы']:
            print("Неверный выбор. Попробуйте снова.")
            continue

        time = current_date.strftime('%H:%M')
        description = input("Введите описание: ")
        amount = float(input("Введите сумму: "))

        if action == 'доходы':
            income = amount
            total_income += amount
            expense = 0
        else:
            income = 0
            expense = amount
            total_expense += expense

        # Добавляем данные в таблицу
        row_data = (time, description, income, expense, (" "), total_income, total_expense)
        sheet.append(row_data)

# Сохраняем рабочую книгу в файл
    wb.save("C:\\Users\\User\\Desktop\\money.xlsx")

# Закрываем рабочую книгу
    wb.close()
