"""
создайте класс `Car`, наследник `Vehicle`
"""

from base import Vehicle
from engine import Engine
from exceptions import LowFuelError

class Car(Vehicle):
    def __init__(self, weight, fuel, _started, fuel_consumption):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def start(self):
        if self._started:
            raise ValueError("Двигатель уже запущен!")
        if self.fuel <= 0:
            raise LowFuelError("Недостаточно топлива для запуска двигателя!")
        self._started = True



    def set_engine(self, engine: Engine):
        if not isinstance(engine, Engine):
            raise ValueError("Переданный объект не является экземпляром класса Engine")
        self.engine = engine