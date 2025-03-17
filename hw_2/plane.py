"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload

class Plane(Vehicle):

    def __init__(self, weight, started=False, fuel=0, fuel_consumption=0, cargo=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self._cargo = cargo  
        self._max_cargo = max_cargo  

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if value < 0:
            raise ValueError("Груз не может быть отрицательным!")
        self._cargo = value

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        if value < 0:
            raise ValueError("Максимальная грузоподъемность не может быть отрицательной!")
        self._max_cargo = value

    def load_cargo(self, amount):
        """
        принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
                 и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload
        """
        if amount + self.cargo <= self.max_cargo:
            self.cargo += amount
        else:
            raise CargoOverload(excess_weight = (amount + self.cargo - self.max_cargo), cargo_weight = self.cargo, max_capacity = self.max_cargo)

    def remove_all_cargo(self):
        """Обнуляет значение cargo и возвращает его предыдущее значение"""
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo