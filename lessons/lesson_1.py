# OOП 1: Основы ООП, Создание первых классов, Атрибуты и Методы классов,
# Принцип ООП - Наследование.

class Car:
    def __init__(self, max_speed, color, model):
        self.max_speed = max_speed
        self.color = color
        self.model = model
if __name__ == '__main__':
    car_honda = Car(160, "silver", "Honda Fit")
    car_subaru = Car(180, "black", "Subaru Fit")
    print(car_honda.max_speed, car_honda.color, car_honda.model)
    print(car_subaru.max_speed, car_subaru.color, car_subaru.model)


