"""
создайте класс `Car`, наследник `Vehicle`

класс Car должен быть наследником Vehicle
добавьте атрибут engine классу Car
объявите метод set_engine, который принимает в себя экземпляр объекта Engine и устанавливает на текущий экземпляр Car

# """
from hw_2.base import Vehicle
from hw_2.engine import Engine


class Car(Vehicle):

    def __init__(self, weight, started=False, fuel=0, fuel_consumption=0, engine=None):
        super().__init__(weight, started, fuel, fuel_consumption)
        self._engine = engine

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value: Engine):
        if not isinstance(value, Engine):
            raise TypeError("Должен быть экземпляром класса Engine")
        self._engine = value

    def set_engine(self, engine: Engine):
        self.engine = engine

