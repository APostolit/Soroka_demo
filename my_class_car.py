#  Модуль my_class_car.py
import streamlit as st
class Car:
    """Автор программы Иванов А.В."""
    class_obj = "Автомобили"  # Объекты класса
    max_speed = 90  # Максимально допустимая скорость на дорогах

    def __init__(self, brand='Ford', weight=900, power=150, colour='Красный'):
        self.brand = brand      # Марка, модель автомобиля
        self.weight = weight    # Вес автомобиля
        self.power = power      # Мощность двигателя
        self.colour = colour    # Мощность двигателя
        self.signal = 'Би-Бип'  # Имитация звука сигнала

    def drive(self):  # Метод двигаться прямо
        st.text("Поехали, двигаемся прямо!")
        st.text("Скорость движения не более -" + str(Car.max_speed))

    def righ(self):  # Метод повернуть на право
        st.text("Едем, поворачиваем руль направо!")

    def left(self):  # Метод повернуть на лево
        st.text("Едем, поворачиваем руль налево!")

    def brake(self):  # Метод тормозить
        st.text("Стоп, активируем тормоз")

    def beep(self):  # Метод подать звуковой сигналь
        st.text("Подан звуковой сигнал")
        st.text(self.signal)


if __name__ == "__main__":
    Car()
