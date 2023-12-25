""" The Adapter Pattern is a structural design pattern that allows
incompatible interfaces to work together.It wraps an existing class
with a new interface, making it compatible with another class.
"""

from abc import ABC, abstractmethod


class Moveable(ABC):
    """Target interface"""

    @abstractmethod
    def move(self):
        """Method for moving."""
        pass


class ElectricCar:
    """Adaptee electric car."""

    def drive(self):
        return "Driving the electric car"


class Vehicle(ABC):
    """Base vehicle class that will be inherited by all vehicles"""

    @abstractmethod
    def move(self):
        """All vehicles should implement this function."""
        pass


class Car(Vehicle):
    """An implementation of car"""

    def move(self):
        return f"{__class__.__name__} is moving"


class Bicycle(Vehicle):
    """An implementation of a bicycle"""

    def move(self):
        return f"{__class__.__name__} is moving"


class ElectricCarAdapter(Moveable):
    """Adapter class that adapts ElectricCar to the Moveable interface"""

    def __init__(self, electric_car: ElectricCar):
        self.electric_car = electric_car

    def move(self):
        return self.electric_car.drive()


# Client code
if __name__ == "__main__":
    car = Car()
    bicycle = Bicycle()

    print(car.move())
    print(bicycle.move())

    electric_car = ElectricCar()
    electric_car_adapter = ElectricCarAdapter(electric_car)
    print(electric_car_adapter.move())
