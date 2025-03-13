"""
создайте класс `Plane`, наследник `Vehicle`
"""
from hw_2.base import Vehicle
from hw_2.exceptions import CargoOverload

class Plane(Vehicle):

    def __init__(self, weight: int, started=False, fuel=0, fuel_consumption=0, cargo=0, max_cargo=0):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, amount_less):
        """принимает число, проверяет, что в сумме с текущим cargo не будет перегруза,
                 и обновляет значение, в ином случае выкидывает исключение exceptions.CargoOverload"""
        if amount_less + self.cargo <= self.max_cargo:
            self.cargo = amount_less + self.cargo
        else:
            raise CargoOverload(f"Перегруз на: {self.max_cargo - (amount_less + self.cargo)}")

    def remove_all_cargo(self):
        """обнуляет значение cargo и возвращает значение cargo, которое было до обнуления"""
        old_cargo = self.cargo
        self.cargo = 0
        return old_cargo