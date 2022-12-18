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

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def print_some(string): #takes no argument and work alone
        print("hey there i am static function in employee class and you typed",string)
        return "Jai mata di"

class Programmer(Employee):

     def __init__(self,aname,asalary,arole,alanguage): #constructor it takes argument and initialize automatically
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguage
    
     def printprog(self):
        return f"The Name is {self.name} and the salary is {self.salary} and the designation is {self.role} and the languages are {self.language}"
    


ajay = Employee("Ajay Chauhan",200000,"Data Engineer") #instance of class
rahul = Employee("Rahul Singh Dangwal",100000,"backend developer")

kani = Programmer("karann","50000","technical content head",["python","c","c++","java"])
Mridhul = Programmer("Mridhula",1000,"java developer",["python","c","c++","java","Django","node.js"])


print(kani.print_some("Le bhaiya omfoo"))
print(kani.printprog())


