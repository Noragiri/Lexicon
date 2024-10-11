# Task: Develop a Simulation System for a Zoo

# Background:
# You are tasked with developing an object-oriented system to simulate a zoo. The system should manage different types of animals and their interactions within the park. The goal is to create a dynamic environment where animals can eat, sleep, and interact with each other and the park's visitors.

# Specifications:

# Basic Objects:


# Animal: The base class for all types of animals. Common attributes may include name, age, and energy level. Basic methods might be to eat, sleep, and make sounds.
class Animal:
    def __init__(self, name, age, species, diet):
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.energy_level = 50  # Default energy level

    def eat(self, food):
        if food == self.diet:
            self.energy_level += 10
            print(
                f"{self.name} the {self.species} eats {food} and now has {self.energy_level} energy."
            )
        else:
            print(f"{self.name} the {self.species} refuses to eat {food}.")

    def sleep(self):
        self.energy_level = 100
        print(f"{self.name} the {self.species} sleeps and now has full energy.")

    def make_sound(self):
        raise NotImplementedError("Each animal must have its own sound.")

    def interact(self, other):
        print(
            f"{self.name} the {self.species} interacts with {other.name} the {other.species}."
        )


# Herbivores and Carnivores: Subclasses that inherit from Animal, with specific characteristics and behaviors.
class Herbivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species, diet="plants")

    def eat(self, food):
        if food == "plants":
            super().eat(food)
        else:
            print(f"{self.name} the {self.species} refuses to eat {food}.")


class Carnivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species, diet="meat")

    def eat(self, food):
        if food == "meat":
            super().eat(food)
        else:
            print(f"{self.name} the {self.species} refuses to eat {food}.")

    def hunt(self, herbivore):
        if isinstance(herbivore, Herbivore):
            herbivore.energy_level -= 20
            self.energy_level += 20
            print(
                f"{self.name} the {self.species} hunts {herbivore.name} the {herbivore.species}!"
            )


# Visitors: A class to represent the visitors in the park, with attributes like name and age.
class Visitor:
    def __init__(self, name, age, food):
        self.name = name
        self.age = age
        self.food = food

    def feed(self, animal):
        animal.eat(self.food)
        print(f"{self.name} feeds {animal.name} the {animal.species}.")


# Features:
# Create specific animal species such as lions, elephants, and giraffes, with unique characteristics and behaviors.
class Lion(Carnivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Lion")

    def make_sound(self):
        print(f"{self.name} the Lion roars!")


class Elephant(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Elephant")

    def make_sound(self):
        print(f"{self.name} the Elephant trumpets!")


class Giraffe(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Giraffe")

    def make_sound(self):
        print(f"{self.name} the Giraffe hums softly.")


# Implement interactions between animals, like hunting or playing.
# Allow visitors to "feed" certain animal species, affecting their energy levels.
# Simulate a day in the zoo, where animals follow their natural routines and interact with visitors.
class Zoo:
    def __init__(self):
        self.animals = []
        self.visitors = []
        self.day_time = "morning"

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def simulate_day(self):
        print(f"--- Simulating a day at the zoo (Time: {self.day_time}) ---")
        for animal in self.animals:
            animal.make_sound()
            animal.sleep()
        for visitor in self.visitors:
            for animal in self.animals:
                visitor.feed(animal)


# Example usage:
zoo = Zoo()

# Add animals
zoo.add_animal(Lion("Simba", 5))
zoo.add_animal(Elephant("Dumbo", 10))
zoo.add_animal(Giraffe("Melman", 7))

# Add visitors
zoo.add_visitor(Visitor("Alice", 30, "plants"))
zoo.add_visitor(Visitor("Bob", 25, "meat"))

# Simulate a day in the zoo
zoo.simulate_day()

# Challenges:

# Managing the energy levels of animals and ensuring they eat and rest regularly.
# Modeling predator-prey relationships in a way that is balanced and doesn’t lead to any species quickly being "eradicated" from the simulation.
# Creating an engaging and interactive experience for the visitor through the interface.
