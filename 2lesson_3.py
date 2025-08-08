#Магические, статичные, классовые методы в классах, множественное наследование.

# Инкапсуляция
class Car:
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model
        self.__fined = True

    def pay_fine(self):
        # setter
        if self.__fined:
            self.__fined = False

    def get_fined(self):
        # getter
        return self.__fined

    def drive_to_location(self, location):
        if self.__fined:
            print(f"Car {self.model} is fined and can not drive everywhere")
        else:
            print(f"Car {self.model} is driving to {location}")

    def __test(self):
        print("Private method")

car_honda = Car(140, "silver", "Honda Fit")
print(car_honda.drive_to_location("Karakol"))
print(car_honda.get_fined())