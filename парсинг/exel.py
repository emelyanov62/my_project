import xlsxwriter
from парсинг2 import arrey
def writer(parametr):
    book = xlsxwriter.Workbook(r'C:\\Users\\User\\Desktop\\сайт.xlsx')
    page = book.add_worksheet('товар')

    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 10)
    page.set_column('C:C', 50)
    page.set_column('D:D', 50)

    for counter in parametr:
        page.write(row, column, counter[0])
        page.write(row, column+1, counter[1])
        page.write(row, column+2, counter[2])
        page.write(row, column+3, counter[3])
        row += 1
        print(row)
    book.close()
    print('готово')
writer(arrey())