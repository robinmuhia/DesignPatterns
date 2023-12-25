"""The Facade Pattern is a structural design pattern that
provides a simplified interface to a set of interfaces in a subsystem.
It defines a higher-level interface that makes the subsystem easier to use,
hiding the complexities of the individual components within the subsystem."""


class Engine:
    """Base engine class"""

    def configure(self):
        return "Configuring the engine"


class Chassis:
    """Basis chassis class"""

    def assemble(self):
        return "Assembling the chassis"


class Components:
    """Base component class."""

    def install(self):
        return "Installing components"


class VehicleFacade:
    """Facade class"""

    def __init__(self):
        self.engine = Engine()
        self.chassis = Chassis()
        self.components = Components()

    def create_vehicle(self):
        result = []
        result.append(self.engine.configure())
        result.append(self.chassis.assemble())
        result.append(self.components.install())
        return result


if __name__ == "__main__":
    facade = VehicleFacade()
    vehicle_creation_result = facade.create_vehicle()

    for step_result in vehicle_creation_result:
        print(step_result)
