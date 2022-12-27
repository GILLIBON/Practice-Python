class Animal:
    
    def __init__(self, name, age, sex, habitat):
        self.name = name # Имя
        self.age = age # Возраст
        self.sex = sex # Пол
        self.habitat = habitat # Ареал обитания
    
    def introduce(self):
        """ Представиться

        Объект сообщает информацию о себе
        """
        print(f'Hello! My name is {self.name}. I am {self.age} y.o. I am {self.sex}, and I live in {self.habitat}.')

class Mammal(Animal):

    def __init__(self, name, age, sex, habitat, food):
        super().__init__(name, age, sex, habitat)
        self.food = food # Любимая еда 

    def tell_about_food(self):
        print(f'My favourite food is {self.food}.')

    def pat(self):
        """ Погладить
        
            Если:
        объект принадлежит классу Человек (Human)
            Тогда:
        Сообщает, что вы не можете его погладить;

            Если: 
        Объект принадлежит классу Собака (Dog) 
            И:
        значение параметра Домашний_или_дикий установлено Дикий
            Тогда:
        Сообщает, что вы не можете его погладить;

            В ином случае:
        Определяет местоимение, которое зависит от пола (sex) объекта.
        Выводит сообщение, содержащее имя и местоимение (pronoun).
        """
        if isinstance(self, Human): # Проверка принадлежности классу Человек (Human)
            print ("You can't pat me, I am human!")

        if (isinstance(self, Dog)  # Проверка принадлежности классу Собака (Dog) 
                and (self.domestic_or_wild == 'wild') # Проверка параметра Домашний_или_дикий (domestic_or_wild)
            ): 
            print ("Arrrgh! Don't try to pet me again!")

        else:
            pronoun = ' '
            if self.sex == 'male':
                pronoun = 'He is'
            else:
                pronoun = 'She is'
            print(f'You petted the {self.name}. {pronoun} happy!')
        
class Human(Mammal):
    def __init__(self, name, age, sex, habitat, food, profession, hobby):
        super().__init__(name, age, sex, habitat, food)
        self.profession = profession # Профессия 
        self.hobby = hobby # Любимое занятие

    def go_to_work(self):
        """ Отправить на работу

        Объект сообщает, что заканчивает заниматься любимым делом (hobby) и уходит на работу.
        Также сообщает о профессии объекта (profession).
        """
        print(f'Okay, I stop {self.hobby} and start work as {self.profession}.')


class Cat(Mammal):
    def __init__(self, name, age, sex, habitat, food, toy, domestic_or_wild):
        super().__init__(name, age, sex, habitat, food)
        self.toy = toy # Любимая игрушка
        self.domestic_or_wild = domestic_or_wild # Домашний или дикий

    def domestic_or_wild_func(self):
        """ Домашний или дикий

            Если:
        объект домашний (domestic)
            Тогда: 
        сообщает об этом;
            
            В ином случае: 
        сообщает, что он дикий (wild).
        """
        if self.domestic_or_wild == 'domestic':
            print ('I am nice domestic kitty.')
        else:
            print('Arrrgh! I am wild.')

    def play(self):
        """ Играть

        Объект сообщает, что играет с любимой игрушкой (toy).
        """
        print(f'Now I play with my favorite toy - {self.toy}.')

class Dog(Mammal):
    def __init__(self, name, age, sex, habitat, food, domestic_or_wild):
        super().__init__(name, age, sex, habitat, food)
        self.domestic_or_wild = domestic_or_wild # Домашний или дикий

    def domestic_or_wild_func(self):
        """ Домашний или дикий

            Если:
        объект домашний (domestic)
            Тогда:
        сообщает об этом;

            В ином случае: 
        сообщает, что он дикий (wild).
        """
        if self.domestic_or_wild == 'domestic':
            print ('I am nice domestic puppy.')
        else:
            print('I am angry wild dog.')


""" -----------------------------------------------------------------
    Примеры объектов:
    
    Animal:
"""
tiger = Animal('Scratchy', 11, 'male', 'savanna')
tiger.introduce()

fish = Animal('Salmon', 2, 'female', 'lake')
fish.introduce()

""" Mammal: 
"""
cow = Mammal('Brownie', 6, 'female', 'grassland', 'herbs')
cow.introduce()
cow.tell_about_food()
cow.pat()

""" Human: 
"""
human1 = Human('Ann', 31, 'female', 'city', 'candies', 'broker', 'watching TV-shows')
human1.introduce()
human1.tell_about_food()
human1.pat()
human1.go_to_work()

human2 = Human('Alex', 22, 'male', 'villiage', 'fries', 'fire watcher', 'workout')
human2.introduce()
human2.tell_about_food()
human2.pat()
human2.go_to_work()

""" Cat: 
"""
cat = Cat('Muffin', 2, 'female', 'city', 'meatballs', 'mouse', 'domestic')
cat.introduce()
cat.tell_about_food()
cat.pat()
cat.play()
cat.domestic_or_wild_func()

""" Dog: 
"""
dog = Dog('Rocky', 3, 'male', 'forest', 'bones', 'wild')
dog.introduce()
dog.tell_about_food()
dog.pat()
dog.domestic_or_wild_func()

