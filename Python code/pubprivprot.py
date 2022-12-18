#Public                   Private                       Protected

class Employee:
    leaves = 10
    _protected = 99 # protected can be used by this class and i=other class derived from it
    __private = 199 #name angling by python
    def __init__(self,aname,asalary,arole): #constructor it takes argument and initialize automatically
        self.name = aname
        self.salary = asalary
        self.role = arole

    
    def printdetails(self):
        return f"name is {self.name} and Salary is {self.salary} and role is {self.role}"

    @classmethod #takes class a input
    def change_leaves(cls,newleaves):
        cls.leaves = newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def print_some(string): #takes no argument and work alone
        print("hey there i am static function in employee class and you typed",string)
        return "Jai mata di"


emp = Employee("Raju", 10000, "Seller")
print(emp._protected)
print(emp._Employee__private)