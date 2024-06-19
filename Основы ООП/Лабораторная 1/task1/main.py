from typing import Union
class Car:
    def __init__(self, hp: Union[int, float], max_speed: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param hp: Мощность двигателя

        :param max_speed: Максимальная скорость

        """
        self.hp = hp
        self.max_speed = max_speed

    def chip_tuning(self, chip: Union[int, float]):
        ...
        """
        Увеличение мощности двигателя
        :return: Измененная мощность 
        """

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
