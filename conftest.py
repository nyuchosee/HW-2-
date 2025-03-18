import pytest

from plane import Plane
from car import Car
from engine import Engine


@pytest.fixture
def engine_test():
    engine = Engine(volume=2.0, pistons=4)
    yield engine


@pytest.fixture
def car_test():
    engine_car = Engine(volume=2.0, pistons=4)
    car = Car(
        weight=1500, _started=False, fuel=70,
        fuel_consumption=12.0
    )
    yield car


@pytest.fixture
def plane_test():
    plane = Plane(
        weight = 10000, fuel = 200.0,
        fuel_consumption = 50.0, max_cargo = 1000
    )
    yield plane
