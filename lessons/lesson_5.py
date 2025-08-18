# from time import sleep
#
# def retry(times):
#     print(f"Retrying... {times}")
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             result = None
#             for i in range(times):
#                 result = function(*args, **kwargs)
#
#             return result
#
#         return wrapper
#     return decorator
#
# @retry(3)
# def open_site(url):
#     print(f"Oenning site: {url}")
#     sleep(2)
#
# open_site("https://www.google.com")









from lessons.lesson_1 import Car

class Money:
    def __init__(self, amount, owner):
        self.amount = amount
        self.owner = owner

    def __str__(self):
        return f"object of Money(amount={self.amount}, owner={self.owner})"

    def __eq__(self, other):
        if self.amount == other.amount:
            return True
        return False

    # gt - greater than: self > other
    # ge - greater than or equal: self >= other
    # lt - less than: self < other
    # le - less than or equal: self <= other
    def __ge__(self, other):
        if self.amount > other.amount:
            return True
        return False

    def __add__(self, other):
        return Money(self.amount + other.amount, self.owner)

money_igor = Money(100, "Igor")
money_syimyk = Money(200, "Syimyk")
print(money_igor)
print(f"Syimyk money is equal to Igor money \
{money_syimyk == money_igor}")
print(f"Syimyk money is greater or equal to Igor money \
{money_syimyk >= money_igor}")
new_money = money_igor + money_syimyk
print(new_money)

car_syimyk = Car(200, "white", "Honda")
print(car_syimyk)