# Листинг 9.2
print('Начальные значения переменным x и y')
x = 10
y = 20
print('x =', x, 'y =', y)

z = (x == 10 and y == 20)
print('(x == 10 and y == 20) ->', z)

z = (x == 10 and y == 10)
print('(x == 10 and y == 10) ->', z)

z = (x == 10 or y == 10)
print('(x == 10 or y == 10) ->', z)

z = (x == 20 or y == 30)
print('(x == 20 or y == 30) ->', z)

z = (x == 10)
print('(x == 10) ->', z)

z = (not x == 10)
print('(not x == 10) ->', z)