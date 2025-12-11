# Листинг 12.2
red_signal = 'Красный'
green_signal = 'Зеленый'
stop = 'Стоять и ждать зеленого сигнала'
start = 'Переходить дорогу'

svetofor = red_signal
if svetofor == red_signal:
    print('Сигнал светофора -', svetofor)
    print(stop)
else:
    print('Сигнал светофора -', svetofor)
    print(start)

print('-'*30)

svetofor = green_signal
if svetofor == red_signal:
    print('Сигнал светофора -', svetofor)
    print(stop)
else:
    print('Сигнал светофора -', svetofor)
    print(start)