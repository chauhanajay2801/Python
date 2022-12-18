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

ajay = Employee("Ajay Chauhan",200000,"Data Engineer") #instance of class
rahul = Employee("Rahul Singh Dangwal",100000,"backend developer")
kani = Employee.from_dash("karann-50000-developer")


print(kani.print_some("Le bhaiya omfoo"))

