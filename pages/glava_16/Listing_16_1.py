# Листинг 16.1
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
        self.signal = 'Би-Бип'  # Имитация звука сигнала

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

print('--- Выводим сведения о классе Car ---')
print('Объекты класса->', Car.class_obj)
print(Car.__doc__)
print('-' * 55)

print('Создаем объект MyCar_1 (значения свойств по умолчанию)')
MyCar_1 = Car()

print('Сведения об объекте MyCar_1 (значения свойств по умолчанию)')
print('Бренд->', MyCar_1.brand)
print('Вес->', MyCar_1.weight, 'кг.')
print('Мощность->', MyCar_1.power, 'лс.')
print('Цвет->', MyCar_1.colour)
print('-' * 55)

print('Создаем объект MyCar_2 и меняем значения свойств')
MyCar_2 = Car('Мерседес', 1200, 250, 'Черный')

print('Сведения об объекте MyCar_2 (с новыми свойствами)')
print('Бренд->', MyCar_2.brand)
print('Вес->', MyCar_2.weight, 'кг.')
print('Мощность->', MyCar_2.power, 'лс.')
print('Цвет->', MyCar_2.colour)