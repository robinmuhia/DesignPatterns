"""
he Strategy Pattern is a behavioral design pattern that defines a family
of algorithms, encapsulates each algorithm, and makes them interchangeable.
It allows the client to choose the appropriate algorithm at runtime.
"""

from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    """Class for implementation of strategy."""

    @abstractmethod
    def move(self):
        """Strategy method for moving."""
        pass


# Concrete Strategies
class CarMoveStrategy(MoveStrategy):
    def move(self):
        return "Driving the car"


class BicycleMoveStrategy(MoveStrategy):
    def move(self):
        return "Riding the bicycle"


# Context class
class Vehicle(ABC):
    """Base vehicle class that will be inherited by all vehicles"""

    def __init__(self, move_strategy):
        self.move_strategy: MoveStrategy = move_strategy

    def perform_move(self):
        return self.move_strategy.move()

    def set_move_strategy(self, move_strategy):
        self.move_strategy = move_strategy


# Concrete Context classes
class Car(Vehicle):
    """An implementation of car"""


class Bicycle(Vehicle):
    """An implementation of a bicycle"""


# Client code
if __name__ == "__main__":
    car_strategy = CarMoveStrategy()
    bicycle_strategy = BicycleMoveStrategy()

    car = Car(car_strategy)
    bicycle = Bicycle(bicycle_strategy)

    # Performing moves
    print(car.perform_move())
    print(bicycle.perform_move())

    # Changing strategies at runtime
    car.set_move_strategy(bicycle_strategy)
    print(car.perform_move())  # Output: Riding the bicycle
