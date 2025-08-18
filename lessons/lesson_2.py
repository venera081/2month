#OOП 2: Другие принципы ООП - Инкапсуляция, Полиморфизм.

class Car:
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model

    def drive_to_location(self, location):
        print(f"Car {self.model} is driving to {location}")

class Bus(Car):
    def __init__(self, max_speed, color, model, number_of_sits):
        super().__init__(max_speed, color, model)
        self.number_of_sits = number_of_sits
    def test(self):
        print(f"Bus test, bus has {self.number_of_sits} sits")

    def drive_to_location(self,location):
        print(f"Bus {self.model} is driving to {location}")

class Truck(Car):
    def drive_to_location(self, location):
        print(f"Truck {self.model} is driving to {location}")

bus = Bus(100, "green", "Mercedes", 40)
bus.drive_to_location("Bishkek")
bus.test()
truck_man = Truck(150, "grey", "MAN")
truck_man.drive_to_location("Karakol")

print(type(1000))
print(type("hello"))
print(type(bus))
print(isinstance(bus, Bus))
print(isinstance(bus, Car))
print(issubclass(Bus, Car))
print(issubclass(Bus, Truck))

# Полиморфизм
car_honda = Car(160, "silver", "Honda Fit")

locations = [bus, truck_man, car_honda]
for location in locations:
    location.drive_to_location("Karakol")
