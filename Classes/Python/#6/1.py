# Vehicle Inheritance
# Create a Python program that models a hierarchy of vehicles using inheritance. Start with a base class
# Vehicle, and then create two or more derived classes (e.g., Car, Bicycle, Motorcycle) that inherit from
# the Vehicle class. Each class should have specific attributes and methods related to the type of vehicle
# it represents.
# 1. Define the Vehicle base class with common attributes such as make, model, and year, and
# methods like start(), stop(), and fuel_up().
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"Maker:{self.make} Model:{self.model} Year:{self.year}"

    def start(self):
        print("Vehicle started")

    def stop(self):
        print("Vehicle stopped")

    def fuel_up(self):
        print("Vehicle fueled up")


# 2. Create derived classes for different types of vehicles, e.g., Car, Bicycle, and Motorcycle. Each
# derived class should inherit from the Vehicle base class and add attributes and methods
# specific to that type of vehicle. For example, the Car class might have attributes like
# num_doors, and the Bicycle class could have attributes like num_gears.
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()} Number of doors:{self.num_doors}"

    def honkHorn(self):
        print("Honk, Honk!")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, num_gears):
        super().__init__(make, model, year)
        self.num_gears = num_gears

    def __str__(self):
        return f"{super().__str__()} Number of gears:{self.num_gears}"

    def ringBell(self):
        print("Ring, Ring!")

    def fuel_up(self):
        print("Fuel with what xdd")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, horse_power):
        super().__init__(make, model, year)
        self.horse_power = horse_power

    def __str__(self):
        return f"{super().__str__()} HP:{self.horse_power}"

    def honkHorn(self):
        print("Honk, Honk!")


# 3. Implement specific methods for each derived class. For instance, the Car class might have a
# method to honk the horn, and the Bicycle class could have a method to ring the bell.
# 4. Create instances of each vehicle type and demonstrate their specific methods and attributes.
# For example, you can create a car, bicycle, and motorcycle, and call methods like start(),
# stop(), and their specific methods like honk_horn() or ring_bell().

car1 = Car("Toyota", "Corola", 2009, 5)
print(car1)
car1.start()
car1.honkHorn()
car1.fuel_up()
car1.stop()

bike1 = Bicycle("Kross", "Level A1", 2014, 6)
print(bike1)
bike1.start()
bike1.ringBell()
bike1.fuel_up()
bike1.stop()

motor1 = Motorcycle("Yamaha", "XSR900", 2023, 115)
print(motor1)
motor1.start()
motor1.honkHorn()
motor1.fuel_up()
motor1.stop()
