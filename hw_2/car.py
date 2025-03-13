"""
создайте класс `Car`, наследник `Vehicle`

класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car

# """

from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):

    def __init__(self, weight: int, started: bool, fuel: int, fuel_consumption: int, engine):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, engine: Engine):
        self.engine = engine

