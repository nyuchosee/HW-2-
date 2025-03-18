from exceptions import LowFuelError, NotEnoughFuel

class Vehicle:
    def __init__(self, weight=1000, fuel=0, fuel_consumption=0.12):
        self.weight = weight
        self._started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    @property
    def started(self):
        return self._started
    
    def start(self):
        if not self._started:
            if self.fuel > 0:
                self._started = True
            else:
                raise LowFuelError("Недостаточно топлива для запуска автомобиля.")

    def move(self, distance):
        if not self._started:
            raise ValueError("Двигатель не запущен! Автомобиль не может двигаться.")

        required_fuel = distance * self.fuel_consumption / 100
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Недостаточно топлива для поездки.")