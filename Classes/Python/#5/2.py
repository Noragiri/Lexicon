import tkinter as tk
from tkinter import messagebox
import random


# Define core animal and zoo logic (same as before)
class Animal:
    def __init__(self, name, age, species, diet):
        self.name = name
        self.age = age
        self.species = species
        self.diet = diet
        self.energy_level = 100  # Full energy to start
        self.hunger_threshold = 40  # Below this, the animal searches for food
        self.max_energy = 100

    def eat(self, food):
        if food == self.diet:
            self.energy_level = min(self.max_energy, self.energy_level + 20)
            return f"{self.name} the {self.species} eats {food}. Energy is now {self.energy_level}."
        else:
            return f"{self.name} the {self.species} refuses to eat {food}."

    def sleep(self):
        self.energy_level = min(self.max_energy, self.energy_level + 30)
        return f"{self.name} the {self.species} sleeps and recovers energy to {self.energy_level}."

    def make_sound(self):
        raise NotImplementedError("Each animal must have its own sound.")

    def interact(self, other):
        if self.energy_level > 20:  # Interaction requires some energy
            self.energy_level -= 10  # Interaction costs energy
            return f"{self.name} the {self.species} interacts with {other.name} the {other.species}."
        else:
            return f"{self.name} the {self.species} is too tired to interact."

    def daily_cycle(self):
        """Simulate a daily routine where the animal loses energy and seeks food/rest"""
        self.energy_level -= 20  # Energy depletes as the day goes on
        if self.energy_level < self.hunger_threshold:
            return f"{self.name} the {self.species} is getting hungry!"
        elif self.energy_level < 20:
            return self.sleep()
        return f"{self.name} the {self.species} continues their day with {self.energy_level} energy."


class Herbivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species, diet="plants")

    def make_sound(self):
        return f"{self.name} the {self.species} makes a peaceful sound."


class Carnivore(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age, species, diet="meat")
        self.hunt_success_rate = 0.5  # 50% chance of a successful hunt

    def hunt(self, prey):
        """Simulate a hunt with a success rate"""
        if (
            isinstance(prey, Herbivore) and self.energy_level < 60
        ):  # Only hunt when energy is low
            success = random.random() < self.hunt_success_rate
            if success:
                prey.energy_level -= 40  # Prey loses energy after being hunted
                return f"{self.name} the {self.species} successfully hunts {prey.name}!"
            else:
                return f"{self.name} the {self.species} failed to catch {prey.name}."
        else:
            return f"{self.name} the {self.species} is not hungry enough to hunt."


class Lion(Carnivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Lion")

    def make_sound(self):
        return f"{self.name} the Lion roars!"


class Elephant(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Elephant")

    def make_sound(self):
        return f"{self.name} the Elephant trumpets!"


class Giraffe(Herbivore):
    def __init__(self, name, age):
        super().__init__(name, age, species="Giraffe")

    def make_sound(self):
        return f"{self.name} the Giraffe hums softly."


class Visitor:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def feed(self, animal, food):
        return animal.eat(food)


class Zoo:
    def __init__(self):
        self.animals = []
        self.visitors = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_visitor(self, visitor):
        self.visitors.append(visitor)

    def simulate_day(self):
        logs = []
        for animal in self.animals:
            logs.append(animal.daily_cycle())  # Each animal follows their daily routine
        return logs


# GUI Implementation
class ZooApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zoo Simulation")

        self.zoo = Zoo()
        self.visitor = Visitor("Alice", 30)

        # Frames
        self.top_frame = tk.Frame(root)
        self.top_frame.pack()

        self.middle_frame = tk.Frame(root)
        self.middle_frame.pack()

        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack()

        # Title
        self.title_label = tk.Label(
            self.top_frame, text="Welcome to the Zoo Simulation!", font=("Arial", 16)
        )
        self.title_label.pack()

        # Animal List
        self.animal_listbox = tk.Listbox(self.middle_frame, width=50, height=10)
        self.animal_listbox.pack()

        # Buttons
        self.add_animal_button = tk.Button(
            self.bottom_frame, text="Add Animals", command=self.add_animals
        )
        self.add_animal_button.pack(side="left")

        self.simulate_button = tk.Button(
            self.bottom_frame, text="Simulate Day", command=self.simulate_day
        )
        self.simulate_button.pack(side="left")

        self.feed_button = tk.Button(
            self.bottom_frame, text="Feed Animal", command=self.feed_animal
        )
        self.feed_button.pack(side="left")

        self.log_text = tk.Text(self.bottom_frame, height=10, width=60)
        self.log_text.pack(side="bottom")

    def add_animals(self):
        """Add animals to the zoo"""
        lion = Lion("Simba", 5)
        elephant = Elephant("Dumbo", 10)
        giraffe = Giraffe("Melman", 7)

        self.zoo.add_animal(lion)
        self.zoo.add_animal(elephant)
        self.zoo.add_animal(giraffe)

        # Display in listbox
        self.animal_listbox.insert(
            tk.END, f"Lion: {lion.name}, Energy: {lion.energy_level}"
        )
        self.animal_listbox.insert(
            tk.END, f"Elephant: {elephant.name}, Energy: {elephant.energy_level}"
        )
        self.animal_listbox.insert(
            tk.END, f"Giraffe: {giraffe.name}, Energy: {giraffe.energy_level}"
        )

    def simulate_day(self):
        """Simulate a day in the zoo and update logs"""
        logs = self.zoo.simulate_day()

        self.log_text.delete(1.0, tk.END)  # Clear previous logs
        for log in logs:
            self.log_text.insert(tk.END, log + "\n")

    def feed_animal(self):
        """Feed selected animal"""
        selected = self.animal_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "No animal selected!")
            return

        animal_index = selected[0]
        animal = self.zoo.animals[animal_index]

        # Visitor feeds the animal
        log = self.visitor.feed(animal, animal.diet)
        self.log_text.insert(tk.END, log + "\n")

        # Update listbox
        self.animal_listbox.delete(animal_index)
        self.animal_listbox.insert(
            animal_index,
            f"{animal.species}: {animal.name}, Energy: {animal.energy_level}",
        )


# Initialize and run the app
root = tk.Tk()
app = ZooApp(root)
root.mainloop()
