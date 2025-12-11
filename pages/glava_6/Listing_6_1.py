# Листинг 6.1
# Формируем строки
str_0 = 'Дама сдавала в багаж'
str_1 = 'Диван,'
str_2 = 'Чемодан, '
str_3 = 'Саквояж,'
str_4 = 'Картину,'
str_5 = 'Корзину, '
str_6 = 'Картонку'
str_7 = 'И маленькую собачонку.'

# Создаем кортеж
bagag = (str_0, str_1, str_2, str_3,
         str_4, str_5, str_6, str_7)
print(bagag[0])
print(bagag[1])
print(bagag[2])
print(bagag[3])
print(bagag[4])
print(bagag[5])
print(bagag[6])
print(bagag[7])
print('-' * 30)

print('Поезд приехал на станцию "Дно"')
print('И там заменили место одно')
print('Решили грузчики так пошутить - ')
str_7 = 'Лохматого пса в багаж посадить'
print(str_7)
print('-' * 30)

# Получение багажа
print('Но получила дама багаж')
print(bagag[1])
print(bagag[2])
print(bagag[3])
print(bagag[4])
print(bagag[5])
print(bagag[6])
print(bagag[7])