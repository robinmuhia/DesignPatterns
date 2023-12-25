"""
The Iterator Pattern is a behavioral design pattern that provides a way to
access the elements of an aggregate object
sequentially without exposing its underlying representation
"""

from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    """Observer pattern implementation."""

    @abstractmethod
    def update(self, vehicle):
        """Update method to be called by the subject
        when there is a state change."""
        pass


class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        """Check if there are more elements in the iteration."""
        pass

    @abstractmethod
    def next(self):
        """Get the next element in the iteration."""
        pass


class Aggregate(ABC):
    @abstractmethod
    def create_iterator(self):
        """Create an iterator for the aggregate."""
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


class VehicleIterator(Iterator):
    """Iterator for vehicle class."""

    def __init__(self, vehicles):
        self._vehicles = vehicles
        self._index = 0

    def has_next(self):
        """Get the next instance"""
        return self._index < len(self._vehicles)

    def next(self):
        """Return the next instance"""
        if self.has_next():
            vehicle = self._vehicles[self._index]
            self._index += 1
            return vehicle
        else:
            raise StopIteration


class TransportFactory(Aggregate):
    """Factory for iterator implementation."""

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

    def create_iterator(self):
        return VehicleIterator(self._observers)


if __name__ == "__main__":
    factory = TransportFactory()
    car_observer = Car()
    bicycle_observer = Bicycle()

    factory.add_observer(car_observer)
    factory.add_observer(bicycle_observer)

    car = factory.create_transport("car")
    bicycle = factory.create_transport("bicycle")

    iterator = factory.create_iterator()
    while iterator.has_next():
        observer = iterator.next()
        print(observer.move())
