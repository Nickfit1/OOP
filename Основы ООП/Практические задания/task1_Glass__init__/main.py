from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0: #and occupied_volume > capacity_volume:
            raise ValueError
        self.occupied_volume = occupied_volume



if __name__ == "__main__":
    glass_1 = Glass(200, 100)
    glass_2 = Glass(500, 300)


    # TODO попробовать инициализировать не корректные объекты
    glass_3 = Glass(0, -1)
    print(glass_3.capacity_volume, glass_3.occupied_volume)
