# Листинг 8.4
letaet = {'Птица', 'Бабочка', 'Самолет'}
vozit = {'Самолет', 'Поезд', 'Корабль'}

print('Заданы множества:')
print('letaet (летает) =', letaet)
print('vozit (возит) =', vozit)
print('-' * 30)

print('Объединили два множества')
print(letaet.union(vozit))
print('-' * 30)

print('Нашли общий элемент у двух множеств')
print(letaet.intersection(vozit))
print('-' * 30)

print('Из множества "letaet" убрали общий элемент')
print(letaet.difference(vozit))
print('-' * 30)

print('Из двух множества убрали общий элемент')
print(letaet.symmetric_difference(vozit))

print('Есть ли "Птица" в множестве letaet->',
      "Птица" in letaet)
print('-' * 30)

# Создаем множество с числами
s_1 = {1,  22, 33, 44}
print('Используем функции для обработки множества s_1')
print('Исходное множество ->', s_1)
print('Количество элементов множества ->', len(s_1))
print('Минимальный элемент множества ->', min(s_1))
print('Максимальный элемент множества ->', max(s_1))
print('Сумма элементов множества ->', sum(s_1))