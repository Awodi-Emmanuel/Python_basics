class car():
 # Class Object Attribute 
    brands = "Mecedis"
    def __init__(self,breed,name): # classs Method 
        self.breed = breed # class object attribute
        self.name = name  # "                 "
x = car("Toyota","Honda") # instantiation of an object
print((x.breed))
print((x.name))
print((x.brands))

class Circle(): 
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius
    def area(self):
        return self.radius*self.radius * Circle.pi
        
myc = Circle(3)
print(myc.area())        

 