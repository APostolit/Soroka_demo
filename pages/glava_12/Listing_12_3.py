# Листинг 12.3
# Братья
brat_1 = 'Старший брат'
brat_2 = 'Средний брат'
brat_3 = 'Младший брат'

# Дворы
dvor_1 = 'Боярский двор'
dvor_2 = 'Купеческий двор'
dvor_3 = 'Болото топкое'

# Кто выпустил стрелу
strela = brat_1
# strela = brat_2
# strela = brat_3

# Инструкции выбора
if strela == brat_1:
    print('Выпустил стрелу - ', strela)
    print('Упала стрела на - ', dvor_1)
elif strela == brat_2:
    print('Выпустил стрелу - ', strela)
    print('Упала стрела на - ', dvor_2)
else:
    print('Выпустил стрелу - ', strela)
    print('Упала стрела на - ', dvor_3)