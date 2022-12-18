# Diamond Shape problem
"""
This is a problem whre class b and class c inherit from a and the class d inhertit the features from  b and c
it creates confusion thet how will it solve the problem and how it will inherit the class and which function it will
perform but it is clear in python
"""

class A:
    def met(self):
        print("This is a method of class A")
    

class B(A):
    def met(self):
        print("This is a method of class B")

class C(A):
    def met(self):
        print("This is a method of class B")

class D(B,C):
    pass


a = A()
b =B()
c =C()
d =D()

d.met()