from homeworks.distance import Distance

dt_1 = Distance(25, "км")
dt_2 = Distance(50, "см")
dt_3 = Distance(90, "мм")
dt_4 = Distance(45, "м")


print(f"Проверка строки: {dt_1}, {dt_2}, {dt_3}, {dt_4}")
print(f"Сложение:\n "
      f"{dt_1} + {dt_4} = {dt_1 + dt_4}\n "
      f"{dt_2} + {dt_3} = {dt_2 + dt_3}\n "
      f"{dt_1} + {dt_3} = {dt_1 + dt_3}")
print(f"Вычитание:\n  "
      f"{dt_1} - {dt_4} = {dt_1 - dt_4}\n "
      f"{dt_2} - {dt_3} = {dt_2 - dt_3}\n "
      f"{dt_1} - {dt_2} = {dt_1 - dt_2}\n "
      f"{dt_1} - {dt_3} = {dt_1 - dt_3}\n "
      f"{dt_4} - {dt_2} = {dt_4 - dt_2}\n "
      f"{dt_4} - {dt_3} = {dt_4 - dt_3}")
try:
    print(f"{dt_4} - {dt_1} = {dt_4 - dt_1}")
    print(f"{dt_3} - {dt_2} = {dt_3 - dt_2}")
    print(f"{dt_2} - {dt_1} = {dt_2 - dt_1}")
    print(f"{dt_3} - {dt_1} = {dt_3 - dt_1}")
    print(f"{dt_2} - {dt_4} = {dt_2 - dt_4}")
    print(f"{dt_3} - {dt_4} = {dt_3 - dt_4}")
except ValueError:
    print("Произошла ошибка, ответ дает отрицательное число")

print(f"Сравнение:\n  "
      f"{dt_1} == {dt_3} -> {dt_1 == dt_3}\n "
      f"{dt_1} < {dt_2} -> {dt_1 < dt_2}\n "
      f"{dt_2} > {dt_3} -> {dt_2 > dt_3}")












