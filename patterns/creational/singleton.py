"""The Singleton Pattern is a creational design pattern that ensures
a class has only one instance and provides a global point of access to
that instance.It is often used when exactly one object is needed to
coordinate actions across the system."""

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


class TransportFactory:
    """An implementation of singleton pattern."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def create_transport(self, transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bicycle":
            return Bicycle()
        else:
            raise ValueError("Invalid transport type")


if __name__ == "__main__":
    factory1 = TransportFactory()
    factory2 = TransportFactory()

    print(factory1 is factory2)  # Output: True (Both instances are the same)

    car = factory1.create_transport("car")
    print(car.move())

    bicycle = factory2.create_transport("bicycle")
    print(bicycle.move())
