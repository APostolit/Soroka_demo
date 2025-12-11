# Листинг 15.3
# Определяем функцию
def my_func(a, b, c): return a + b + c

x, y, z = 1, 2, 3
print('Аргументы числа, rez1 = ', my_func(x, y, z))

x = ['Иванов ', 'Семен ', 'Петрович']
rez2 = my_func(x[0], x[1], x[2])
print('Аргументы символы, rez2 = ', rez2)