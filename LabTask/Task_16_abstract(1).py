from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("Car is starting.")

    def stop(self):
        print("Car is stopping.")

class MotorCycle(Vehicle):
    def __init__(self):
        pass

    def start(self):
        print("MotorCycle is starting.")

    def stop(self):
        print("MotorCycle is stopping.")

# Create objects
car = Car()
car.start()

# Attempting to instantiate abstract class
try:
    vehicle = Vehicle()  # Raises TypeError
except TypeError as e:
    print(e)
