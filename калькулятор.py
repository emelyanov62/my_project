number = int(input('Введите число: '))
number2 = int(input('Введите число: '))
sign = input('Введите знак: ')

def total(x, s, y):
    if s == '+':
        tot = (x + y)
    elif s == '-':
        tot = (x - y)
    elif s == '*':
        tot = (x * y)
    elif s == '/':
        tot = (x / y)
    return tot
a = total(number, sign, number2)
print(a)