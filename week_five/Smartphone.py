# Base class: Smartphone
class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand          # Public attribute
        self.model = model          # Public attribute
        self._battery = battery     # Protected attribute
        self.__imei = "12345XYZ"    # Private attribute (hidden)

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number} 📞"

    def battery_status(self):
        return f"Battery: {self._battery}% 🔋"

    # Encapsulation (controlled access)
    def get_imei(self):
        return f"IMEI: {self.__imei}"


# Derived class: AdvancedSmartphone (Inheritance + Polymorphism)
class AdvancedSmartphone(Smartphone):
    def __init__(self, brand, model, battery, os):
        super().__init__(brand, model, battery)  # Call parent constructor
        self.os = os

    # Polymorphism: overriding call method
    def call(self, number):
        return f"{self.brand} {self.model} ({self.os}) is making a video call to {number} 🎥📱"


# Create objects
phone1 = Smartphone("Nokia", "3310", 90)
phone2 = AdvancedSmartphone("Apple", "iPhone 15", 75, "iOS")

# Testing functionality
print(phone1.call("08012345678"))      # Normal call
print(phone1.battery_status())         
print(phone1.get_imei())               # Accessing private attribute via method

print(phone2.call("08098765432"))      # Polymorphic call (video call)
print(phone2.battery_status())

