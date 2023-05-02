import random

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def description(self):
        return f"Your name is {self.name}, your age is {self.age}"


class Car(Person):
    def __init__(self, name: str, age: int, car: str):
        super().__init__(name, age)
        self.car = car
        
    def description(self):
        return f"Your name is {self.name}, your age is {self.age}, your car is {self.car}"
        

class Luck(Person):
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.luck = random.randint(100, 200)
        
        
    def desc(self):
        if self.luck > 150:
            luck = f"You have very good lucky with score {self.luck}"
        elif self.luck > 130 and self.luck < 150:
            luck = f"You have good lucky with score {self.luck}"
        else:
            luck = f"You have normal lucky with score {self.luck}"

        return f"Your name is {self.name}, Your age is {self.age}, and {luck}"


Person = Person('Haikal', 18)
desc = Person.description()
print(desc)
Car = Car('Haikal', 18, 'Lamborghini')
desc = Car.description()
print(desc)
Luck = Luck('haikal', 18)
desc = Luck.desc()
print(desc)