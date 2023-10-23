import openpyxl


global photo, description, urls
wb = openpyxl.load_workbook('C:\\Users\\User\\Desktop\\mebel.xlsx')
sheet = wb.active
skip_first_row = True
for row in sheet.iter_rows(values_only=True):
    if skip_first_row:
        skip_first_row = False
        continue
description, photo, urls = row[:3]
print(f"Description: {description}, Photo URL: {photo}, URLs: {urls}")
