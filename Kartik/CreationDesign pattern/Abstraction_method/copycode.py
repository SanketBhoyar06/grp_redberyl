from abc import ABC, abstractmethod

# Abstract Product A
class Car(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product A1
class SedanCar(Car):
    def display(self):
        return "Sedan Car"

# Concrete Product A2
class SportsCar(Car):
    def display(self):
        return "Sports Car"

# Abstract Product B
class Bike(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Product B1
class CruiserBike(Bike):
    def display(self):
        return "Cruiser Bike"

# Concrete Product B2
class SportBike(Bike):
    def display(self):
        return "Sport Bike"

# Abstract Factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car:
        pass

    @abstractmethod
    def create_bike(self) -> Bike:
        pass

# Concrete Factory for Vehicles
class ConcreteVehicleFactory(VehicleFactory):
    def create_car(self) -> Car:
        return SportsCar()

    def create_bike(self) -> Bike:
        return CruiserBike()

# Client Code
def create_vehicles(factory: VehicleFactory):
    car = factory.create_car()
    bike = factory.create_bike()

    print(car.display())
    print(bike.display())

# Example usage
vehicle_factory = ConcreteVehicleFactory()
create_vehicles(vehicle_factory)
