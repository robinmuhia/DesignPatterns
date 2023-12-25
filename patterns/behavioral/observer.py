"""The Observer Pattern is a behavioral design pattern where an object,
known as the subject, maintains a list of its dependents, called observers,
that are notified of any state changes,
typically by calling one of their methods. """

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Implements the observer pattern."""

    @abstractmethod
    def update(self, vehicle):
        """Update method to be called by the subject
        when there is a state change."""
        pass


class Vehicle(Observer, ABC):
    """Base vehicle class that will be inherited by all vehicles"""

    @abstractmethod
    def move(self):
        """All vehicles should implement this function."""
        pass


class Car(Vehicle):
    """An implementation of car"""

    def update(self, vehicle):
        print(f"New {vehicle.__class__.__name__} created!")

    def move(self):
        return f"{__class__.__name__} is moving"


class Bicycle(Vehicle):
    """An implementation of a bicycle"""

    def update(self, vehicle):
        print(f"New {vehicle.__class__.__name__} created!")

    def move(self):
        return f"{__class__.__name__} is moving"


class TransportFactory:
    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, vehicle):
        for observer in self._observers:
            observer.update(vehicle)

    def create_transport(self, transport_type):
        if transport_type == "car":
            vehicle = Car()
        elif transport_type == "bicycle":
            vehicle = Bicycle()
        else:
            raise ValueError("Invalid transport type")

        self.notify_observers(vehicle)

        return vehicle


if __name__ == "__main__":
    factory = TransportFactory()
    car_observer = Car()
    bicycle_observer = Bicycle()

    factory.add_observer(car_observer)
    factory.add_observer(bicycle_observer)

    car = factory.create_transport("car")
    print(car.move())

    bicycle = factory.create_transport("bicycle")
    print(bicycle.move())
