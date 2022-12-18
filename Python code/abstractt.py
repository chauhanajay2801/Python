from abc import ABC , abstractclassmethod

class Shape(ABC): #the abstract method is a method that once u declare and then any class inherit it must have that abstract method
    @abstractclassmethod #for that we need abc meta class
    def printarea(self): # we cant make instances of this class
        return 0

class Rectangle(Shape):
    type ="Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.breadth*self.length

rec = Rectangle()
print(rec.printarea())
 