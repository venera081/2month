class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}."
              f"У меня {self.higher_education} ")

class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, hobby, friend_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.hobby = hobby
        self.friend_name = friend_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Я подруга {self.friend_name}. Мы {self.hobby}. "
              f"Я родилась {self.birth_date}. Моя профессия {self.occupation}. У меня"
                f" {self.higher_education}")

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name, classmate_name):
        super().__init__(name, birth_date, occupation, higher_education)
        self.group_name = group_name
        self.classmate_name = classmate_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Я одноклассница {self.classmate_name}."
              f" Учились вместе в {self.group_name}. Я родилась {self.birth_date}. Моя профессия "
               f"{self.occupation}. У меня {self.higher_education}")


person = Person("Венера", "8.11.2009", "студентка", "нет высшего образования")
person_1 = Person("Венеры", "8.11.2009", "студентка", "нет высшего образования")
person_1.introduce()
classmate = Classmate("Вика", "15.9.2009", "студентка",
                      "нет высшего образования", "9Д", person_1.name)
classmate2 = Classmate("Раяна", "26.12.2009", "студентка",
"нет высшего образования", "9Д", person_1.name)
friend = Friend("Асема", "5.01.2009", "модель",
"нет высшего образования", "любим одну музыкальную группу", person_1.name)

for people in [classmate, classmate2, friend]:
    people.introduce()


