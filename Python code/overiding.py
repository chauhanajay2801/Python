class A:
    classvar1 = "I live in class a"
    def __init__(self):
        self.var1 = "I am in class A constructor"
        self.classvar1 = "I am a instance variable in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I live in class B"

    def __init__(self):
        super().__init__()#explaination below
        """
        once the constructor is override there is no role of the previous class and no matter how we cant call the old variables
        and in order to do that we need "super().__init__()" 
        """
        self.var1 = "I am in class B constructor"
        self.classvar1 = "I am a instance variable in class B"
        print(super().classvar1)


a = A()
b = B()

print(b.special,b.var1,b.classvar1)
"""
first it will search for instance variable and if it do not find in class b as it is a class variable then it will jump to 
the main class it is derived from and the print the instance variable, if the variable is not in the main class them 
it will print the class variable named as class var1 and if that also is not present it will go to the class a variable
"""