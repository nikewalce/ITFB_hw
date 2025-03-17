"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, message="Низкий уровень топлива!", fuel_level: float = 0):
        self.fuel_level = fuel_level
        super().__init__(f"{message} Текущий уровень топлива: {fuel_level} л.")


class NotEnoughFuel(Exception):
    def __init__(self, message="Не хватает топлива!", required_fuel: float = 0, available_fuel: float = 0):
        self.required_fuel = required_fuel
        self.available_fuel = available_fuel
        super().__init__(f"{message} Требуется: {required_fuel} л, доступно: {available_fuel} л.")


class CargoOverload(Exception):
    def __init__(self, message="Перегруз!", excess_weight: float = 0, cargo_weight: float = 0, max_capacity: float = 0):
        self.excess_weight = excess_weight
        self.cargo_weight = cargo_weight
        self.max_capacity = max_capacity
        super().__init__(f"{message} Перегруз: {excess_weight} кг! Текущий груз: {cargo_weight} кг, лимит: {max_capacity} кг.")
