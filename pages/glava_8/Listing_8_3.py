# Листинг 8.3
# Множества с днями недели
Days1 = {"Понедельник",  "Вторник", "Среда", "Четверг"}
Days2 = {"Пятница", "Суббота", "Воскресенье"}
Days3 = {"Вторник", "Среда"}
print('Заданы множества:')
print('Days1 =', Days1)
print('Days2 =', Days2)
print('Days3 =', Days3)
print('-' * 30)

print('Объединение множеств Days1 | (Days2')
print(Days1 | Days2)
print('-' * 30)

print('Пересечение множеств Days1 & (Days3')
print(Days1 & Days3)
print('-' * 30)

print('Разница множеств Days1 - Days3')
print(Days1 - Days3)
print('-' * 30)

print('Симметричная разность двух множеств  Days1 ^ (Days3')
print(Days1 ^ Days3)