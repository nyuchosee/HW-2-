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

    @started.setter
    def started(self, value):
        if not isinstance(value, bool):
            raise ValueError("Состояние двигателя должно быть True или False")
        self._started = value

    def start(self):
        if not self.started:  # Теперь работаем через property
            if self.fuel > 0:
                self.started = True  # Используем сеттер
            else:
                raise LowFuelError("Недостаточно топлива для запуска автомобиля.")

    def move(self, distance):
        if not self.started:
            raise ValueError("Двигатель не запущен! Автомобиль не может двигаться.")

        required_fuel = distance * self.fuel_consumption / 100
        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
        else:
            raise NotEnoughFuel("Недостаточно топлива для поездки.")