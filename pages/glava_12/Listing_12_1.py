# Листинг 12.1
doroga_rovno = 'Ровная дорога'
doroga_yama = 'Яма на дороге'
tormoz = 'Нужно сбавить скорость и объехать яму'
rovno = 'Дорога ровная, можно ехать вперед'

print(rovno)
doroga = rovno
if doroga == doroga_yama:
    print(tormoz)
    doroga = rovno
print(rovno)

print('-'*30)

print(rovno)
doroga = doroga_yama
if doroga == doroga_yama:
    print(tormoz)
    doroga = rovno
print(rovno)