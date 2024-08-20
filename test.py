# test.py

class Animal:
    pass

class Dog(Animal):
    def __init__(self, barkSound = "Unknown"):
        print("Animal Cons - bs = ", barkSound)

    def Bark():
        print("bark sound " , self.barkSound)

class Jack(Dog):
    def Bark(self):
        print("Jack barks")


