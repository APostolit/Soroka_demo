# Листинг 16.2
class Car:
    """Автор программы Питоша"""
    class_obj = "Автомобили"  # Объекты класса
    max_speed = 90  # Максимально допустимая скорость на дорогах

    def __init__(self, brand='Ford', weight=900,
                 power=150, colour='Красный'):
        self.brand = brand      # Марка, модель автомобиля
        self.weight = weight    # Вес автомобиля
        self.power = power      # Мощность двигателя
        self.colour = colour    # Мощность двигателя
        self.signal = 'Би-Бип'  # Имитация зука сигнала

    def drive(self):  # Метод двигаться прямо
        print("Поехали, двигаемся прямо!")
        print("Скорость движения не более -", Car.max_speed)

    def righ(self):  # Метод повернуть на право
        print("Едем, поворачиваем руль направо!")

    def left(self):  # Метод повернуть на лево
        print("Едем, поворачиваем руль налево!")

    def brake(self):  # Метод тормозить
        print("Стоп, активируем тормоз")

    def beep(self):  # Метод подать звуковой сигналь
        print("Подан звуковой сигнал")
        print(self.signal)

def drive_car(MyCar):
    print('----- Поехал автомобиль', MyCar.brand, '-----')
    MyCar.drive()  # Двигается прямо
    MyCar.righ()  # Поворачиваем направо
    MyCar.drive()  # Двигается прямо
    MyCar.left()  # Поворачиваем налево
    MyCar.drive()  # Двигается прямо
    MyCar.beep()  # Подаем звуковой сигнал
    MyCar.brake()  # Тормозим
    print('-' * 50)
    return

MyCar_1 = Car()
print('Создан автомобиль', MyCar_1.brand, 'цвет-', MyCar_1.colour)
drive_car(MyCar_1)

MyCar_2 = Car('Мерседес', 1200, 250, 'Черный')
print('Создан автомобиль', MyCar_2.brand, 'цвет-', MyCar_2.colour)
drive_car(MyCar_2)