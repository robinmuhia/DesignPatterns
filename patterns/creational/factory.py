"""This design pattern provides an interface for creating objects
in a super class but allows subclasses to alter
the type of objects that will be created."""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Base vehicle class that will be inheited by all vehicles"""

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
    """Class that instantiates Vehicle class"""

    def create_transport(self, transport_type):
        if transport_type == "car":
            return Car()
        elif transport_type == "bicycle":
            return Bicycle()
        else:
            raise ValueError("Invalid transport type")


if __name__ == "__main__":
    factory = TransportFactory()

    car = factory.create_transport("car")
    print(car.move())

    bicycle = factory.create_transport("bicycle")
    print(bicycle.move())
