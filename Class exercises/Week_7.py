"""
Classes class exercises
----------------------
Note: Remember classes are object creators, and we utilise their methods after creating an instance of the class.
(Slide 16 of Week 7 & 8
"""

# Q1 - A person class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Q2 - A rectangle class

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

# Q3 - A bank account class

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

# Q4 - A car class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        print(f"{self.year} {self.make} {self.model}")


# Test the classes
person = Person("Alice", 25)
person.greet()

rectangle = Rectangle(5, 10)
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())

bank_account = BankAccount(1000)
print("Initial Balance:", bank_account.get_balance())
bank_account.deposit(500)
print("Balance after deposit:", bank_account.get_balance())
bank_account.withdraw(200)
print("Balance after withdrawal:", bank_account.get_balance())

car = Car("Toyota", "Camry", 2022)
car.description()

"""
Classes inheritance class exercises
----------------------
(Slide 22 of Week 7 & 8
"""

# Q1 - Animal class inheritance
class Animal:
    def speak(self):
        print("I am an animal.")


class Dog(Animal):
    def speak(self):
        print("I am a dog.")

# Q2 - Shape class inheritance
class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Q3 - Vehicle class inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def get_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"


# Test the classes
animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

rectangle = Rectangle(5, 10)
print("Rectangle Area:", rectangle.area())

triangle = Triangle(4, 6)
print("Triangle Area:", triangle.area())

car = Car("Toyota", "Camry", 2022)
print("Car Info:", car.get_info())

motorcycle = Motorcycle("Honda", "CBR600RR", 2021)
print("Motorcycle Info:", motorcycle.get_info())
