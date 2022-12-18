# dunder method - method which start and ends with __
class Employee:
    leaves = 10
    def __init__(self,aname,asalary,arole): #constructor it takes argument and initialize automatically
        self.name = aname
        self.salary = asalary
        self.role = arole

    
    def printdetails(self):
        return f"name is {self.name} and Salary is {self.salary} and role is {self.role}"

    @classmethod #takes class a input
    def change_leaves(cls,newleaves):
        cls.leaves = newleaves

    def __add__(self,other):
        return self.salary + other.salary

    def __truediv__(self,other): #check other dunder methods from the documentation
        return self.salary / other.salary

    def __repr__(self): #to beautify it
        return f"Employee({self.name},{self.salary},{self.role})"

emp1 = Employee("Ajay", 800, "Django Developer")
emp2 = Employee("Vijay", 40, "Cleaner")
print(emp1+emp2) #it jumps to the add method written as dunder method
print(emp1/emp2)
print(emp1)

    