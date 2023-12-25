"""The Builder Pattern is a creational design pattern that
separates the construction of a complex object from its representation. It
allows the same construction
process to create different representations of an object. """

from abc import ABC, abstractmethod


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


class VehicleBuilder(ABC):
    """This abstract class is used by the sub-classes to build a car."""

    @abstractmethod
    def build(self):
        """Build the vehicle."""
        pass

    @abstractmethod
    def get_result(self):
        """Get the constructed vehicle."""
        pass


class CarBuilder(VehicleBuilder):
    def __init__(self):
        """Constructor for the car."""
        self.vehicle = Car()

    def build(self):
        pass

    def get_result(self):
        return self.vehicle


class BicycleBuilder(VehicleBuilder):
    def __init__(self):
        """Constructor for the bicycle."""
        self.vehicle = Bicycle()

    def build(self):
        pass

    def get_result(self):
        return self.vehicle


class VehicleDirector:
    """Implementation of the vehicle director class."""

    def __init__(self, builder: VehicleBuilder):
        """Constructor for this class"""
        self.builder = builder

    def construct(self):
        """Build the vehicle itself."""
        self.builder.build()


if __name__ == "__main__":
    car_builder = CarBuilder()
    director = VehicleDirector(car_builder)
    director.construct()
    car = car_builder.get_result()
    print(car.move())

    bicycle_builder = BicycleBuilder()
    director = VehicleDirector(bicycle_builder)
    director.construct()
    bicycle = bicycle_builder.get_result()
    print(bicycle.move())
