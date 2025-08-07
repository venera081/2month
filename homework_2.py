class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education
    def introduce(self):
        print(f"Меня зовут {person.name}, я родилась {self.birth_date} и я {self.occupation} ")
class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я подруга {person_1.name}, и мы {self.hobby}, "
              f"я родилась {self.birth_date}, я {self.occupation}")
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одноклассница {person_1.name},"
              f" учились вместе в {self.group_name}, я родилась {self.birth_date}, я {self.occupation} ")

person = Person("Венера", "8.11.2009", "студентка", False)
#убрала вызов introduce, потому что распечатывалось 2 раза
person_1 = Person("Венеры", "8.11.2009", "студентка", False)
person_1.introduce()
classmate = Classmate("Вика", "15.9.2009", "студентка", False, "9Д")
classmate2 = Classmate("Раяна", "26.12.2009", "студентка", False,"9Д")
friend = Friend("Асема", "5.01.2009", "модель", False, "любим одну "
                                                       "музыкальную группу")
for people in [classmate, classmate2, friend]:
    people.introduce()








