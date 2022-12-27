class Animal:
    def __init__(self, name, age, sex):
        self.name = name # Имя
        self.age = age # Возраст
        self.sex = sex # Пол
    
class Mammal(Animal):
    def __init__(self, name, age, sex, food):
        super().__init__(name, age, sex,)
        self.food = food # Любимая еда 
        
class Human(Mammal):
    def __init__(self, name, age, sex, food, profession, hobby):
        super().__init__(name, age, sex, food)
        self.profession = profession # Профессия 
        self.hobby = hobby # Любимое занятие

class Student(Human):
    def __init__(self, name, age, sex, food, profession, hobby, favorite_lesson, amount_homework):
        super().__init__(name, age, sex, food, profession, hobby)
        self.favorite_lesson = favorite_lesson # Любимый урок
        self.amount_homework = amount_homework # Кол-во сданных ДЗ


    def tell_about_yourself(self):
        """ Рассказать о себе 
        
            Выводит информацию об объекте
        """
        print(f'Hi! My name is {self.name}, I am {self.age} y.o. I like to eat {self.food}. Now I am {self.profession}, but my favourite hobby is {self.hobby}. \
I really like lessons of {self.favorite_lesson}, I already complete {self.amount_homework} homeworks!\n')

    def __cmp__(self, other):
        """ Сравнение количества ДЗ

        Считаем разницу количества ДЗ у двух студентов.
            Если: 
        Результат < 0
            Тогда:
        Кол-во дз первого меньше кол-ва дз второго;

            Если:
        Результат > 0
            Тогда:
        Кол-во дз первого больше кол-ва дз второго;

            Если:
        Результат == 0
            Тогда:
        Кол-во дз обоих одинаково.
        """
        if (self.amount_homework - other.amount_homework) < 0:
            print(f'{self.name} did less homework than {other.name}.')

        elif (self.amount_homework - other.amount_homework) > 0:
            print(f'{self.name} did more homework than {other.name}.')
            
        elif (self.amount_homework - other.amount_homework) == 0:
            print(f'{self.name} and {other.name} did the same amount of homework.')


""" Объекты класса Student: 
"""
student1 = Student('Mike', 19, 'male', 'pizza', 'student', 'skateboarding', 'geography', 12)
student1.tell_about_yourself()

student2 = Student('Zoe', 18, 'female', 'vegetables', 'student', 'doing homework', 'math', 17)
student2.tell_about_yourself()

"""Сравниваем количество дз двух студентов:
"""
student1.__cmp__(student2)