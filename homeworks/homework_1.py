class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education


person_1 = Person("venera", 8.11, "student", False )
person_2 = Person("vika", 15.9, "student", False)
person_3 = Person("asema", 5.1, "model", False)
print(f"1)Имя: {person_1.name}, дата рождения: {person_1.birth_date},"
      f" профессия: {person_1.occupation}, высшее образование: {person_1.higher_education}")
print(f"2)Имя: {person_2.name}, дата рождения: {person_2.birth_date},"
      f" профессия: {person_2.occupation}, высшее образование: {person_2.higher_education}")
print(f"3)Имя: {person_3.name}, дата рождения: {person_3.birth_date},"
      f" профессия: {person_3.occupation}, высшее образование: {person_3.higher_education}")
