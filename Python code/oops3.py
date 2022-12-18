class Employee:
    leaves = 10
    def __init__(self,aname,asalary,arole): #constructor it takes argument and initialize automatically
        self.name = aname
        self.salary = asalary
        self.role = arole

    
    def printdetails(self):
        return f"name is {self.name} and Salary is {self.salary} and role is {self.role}"

    @classmethod #takes class a input
    def change_leaves(cls,newleaves):#can be accesed by instances and by class also
        cls.leaves = newleaves


ajay = Employee("Ajay Chauhan",200000,"Data Engineer") #instance of class
rahul = Employee("Rahul Singh Dangwal",100000,"backend developer")

ajay.change_leaves(34)
print(ajay.leaves)

