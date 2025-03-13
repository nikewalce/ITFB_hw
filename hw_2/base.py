from abc import ABC
from hw_2.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    def __init__(self, weight: int = 0, started: bool = False, fuel: int = 0, fuel_consumption: int = 0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        """Необходимо проверить состояние started.
        И если не started, то нужно проверить, что топлива больше нуля,
        и обновить состояние started, иначе нужно выкинуть исключение exceptions.LowFuelError"""
        if self.started:
            raise ValueError("Двигатель уже запущен!")
        elif self.started == False:
            if self.fuel > 0:
                self.started = True
                return True
            else:
                raise LowFuelError("Низкий уровень топлива!")

    def move(self, distance: int):
        """проверяет, что топлива достаточно для преодоления переданной дистанции
         (вплоть до полного расхода), и изменяет количество оставшегося топлива,
         иначе выкидывает исключение exceptions.NotEnoughFuel"""
        if not self.started:
            raise ValueError("Двигатель заглушен!")
        required_fuel = (distance * self.fuel_consumption) / 100
        if self.fuel < required_fuel:
            raise NotEnoughFuel("Не хватает топлива!")

        self.fuel -= required_fuel
