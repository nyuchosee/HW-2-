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
    
    def load_cargo(self, amount):
        if self._cargo + amount <= self.max_cargo:
            self._cargo += amount
        else:
            raise CargoOverload("Груз превышает максимальную вместимость.")

    def remove_all_cargo(self):
        remove_all = self._cargo
        self._cargo = 0
        return remove_all

