#Множественное наследование

class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Гав гав")

class Cat(Animal):
    def speak(self):
        super().speak()
        print("Мяу мяу")

class CatDog:
    def speak(self):
        print("Гав мяу")

kotopes = CatDog()
kotopes.speak()
print(CatDog.mro())






class User:
    # переменные классы
    total_users = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        User.total_users +=1

    @classmethod
    def get_total_users(cls):
        return cls.total_users

    @staticmethod
    def validate_email(email):
        return "@" in email

user_igor = User("Igor", "igor@gmail.com")
user_kurmanbek = User("Kurmanbek", "kurmanbek@gmail.com")
print(User.total_users)
print(User.get_total_users())
print(User.validate_email("igor@gmail.com"))







# Декораторы

# def printer(function):
#     def wrapper(*args, **kwargs):
#         print(f"До вызова функции {function.__name__}")
#         result = function(*args, **kwargs)
#         print(f"После вызова функции {function.__name__}")
#         return result
#     return wrapper
#
# def hello_world():
#     print("Hello World")
#
# def add_numbers(a, b):
#     return a + b
#
#
# hello_world()
# result = add_numbers(3, 6)
# print(printer(__name__))

