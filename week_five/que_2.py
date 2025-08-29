# Base class
class Vehicle:
    def move(self):
        pass  # Abstract-like method (to be overridden by subclasses)


# Car class
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


# Plane class
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


# Boat class
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# Demonstration of polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

