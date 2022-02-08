# INHERITANCE 
class Animal():
    def __init__(self):
        print("ANIMAL CREATED")
    def whoAmI(self):
        print("ANIMAL")
    def eat(self):
        print('EATINg')
class Dog(Animal): 
        def __init__(self):
            # Animal.__init__(self)
            print("DOG CREATED")  
        def bark(self):
            print("WOOF") 
        def eat(self):
            print("DOG EATING")              
mydog = Dog()
mydog.whoAmI()
mydog.eat()          