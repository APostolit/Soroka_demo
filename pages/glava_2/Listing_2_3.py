# Листинг 2.3
a = 'Стоимость товара - '
b = 100
b = str(b)
c = ' руб.'
try:
    d = a + b + c
    print(d)
except TypeError:
    print('Ошибка - сложение переменных разных типов')