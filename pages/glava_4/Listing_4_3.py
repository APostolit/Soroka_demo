# Листинг 4.3
# Формируем строки
str_1 = '\n В траве сидел кузнечик,'
str_2 = '\n Совсем как огуречик, '
str_3 = '\n Зелененький он был.'
str_4 = '\n Представьте себе,'

# Сложение строк
song = str_1 * 2
song += str_2
song += str_3
song = song + str_4
song = song + str_4
song += str_2
song = song + str_4
song = song + str_4
song += str_3
print(song)
# Умножение строк
print('-' * 30)