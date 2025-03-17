from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight: int = 0, started: bool = False, fuel: int = 0, fuel_consumption: int = 0):
        self._weight = weight
        self._started = started
        self._fuel = fuel
        self._fuel_consumption = fuel_consumption

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Вес не может быть отрицательным!")
        self._weight = value

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        if value < 0:
            raise ValueError("Топливо не может быть отрицательным!")
        self._fuel = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        if value < 0:
            raise ValueError("Расход топлива не может быть отрицательным!")
        self._fuel_consumption = value

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        if not isinstance(value, bool):
            raise ValueError("Состояние двигателя должно быть True или False!")
        self._started = value

    def start(self):
        """Необходимо проверить состояние started.
                И если не started, то нужно проверить, что топлива больше нуля,
                и обновить состояние started, иначе нужно выкинуть исключение exceptions.LowFuelError"""
        if self.started:
            raise ValueError("Двигатель уже запущен!")
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError(fuel_level = self.fuel)

    def move(self, distance: int):
        """проверяет, что топлива достаточно для преодоления переданной дистанции
                 (вплоть до полного расхода), и изменяет количество оставшегося топлива,
                 иначе выкидывает исключение exceptions.NotEnoughFuel"""
        if not self.started:
            raise ValueError("Двигатель заглушен!")
        required_fuel = (distance * self.fuel_consumption) / 100
        if self.fuel < required_fuel:
            raise NotEnoughFuel(required_fuel=required_fuel, available_fuel=self.fuel)

        self.fuel -= required_fuel