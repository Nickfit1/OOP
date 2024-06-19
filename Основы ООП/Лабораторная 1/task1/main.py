from typing import Union
import doctest


class Car:
    def __init__(self, hp: Union[int, float], max_speed: Union[int, float], brake_distance: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param hp: Мощность двигателя
        :param max_speed: Максимальная скорость
        :param brake_distance: Тормозной путь

        """
        self.hp = hp
        self.max_speed = max_speed


    def chip_tuning(self, chip: Union[int, float]):
        ...
        """
        Увеличение мощности двигателя
        :param chip: Процент, на который увеличивается мощность
        :return: Измененная мощность 
        Примеры:
        >>> car = Car(150, 200)
        >>> car.chip_tuning()
        """


    def good_brakes(self, brake_coeff):
        ...
        """
        Уменьшение тромозного пути
        :param brake_coeff: тормозной коэффициент колодок
        :return: Измененный тормозной путь
        Примеры:
        >>> car = Car(150, 200)
        >>> car.good_brakes()
        """


class Man:
    def __init__(self, age: int, weight: Union[int, float], strong: int):
        """
               Создание и подготовка к работе объекта "Человек"

               :param age: Возраст
               :param weight: Вес
               :param strong: Сила

        """
        self.age = age
        self.weight = weight
        self.strong = strong






if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
