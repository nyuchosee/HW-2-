"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle
from exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption)
        self._cargo = 0
        self.max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Груз должен быть положительным числом.")
        if value > self.max_cargo:
            raise CargoOverload("Груз превышает максимальную вместимость.")
        self._cargo = value

    def load_cargo(self, amount):
        self.cargo = self._cargo + amount

    def remove_all_cargo(self):
        remove_all = self._cargo
        self._cargo = 0
        return remove_all

