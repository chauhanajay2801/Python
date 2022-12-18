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

    @classmethod
    def from_dash(cls,string):
        #params = string.split("-")
        #return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))#one liner for upper two line
    
  

ajay = Employee("Ajay Chauhan",200000,"Data Engineer") #instance of class
rahul = Employee("Rahul Singh Dangwal",100000,"backend developer")
kani = Employee.from_dash("karann-50000-developer")

#ajay.change_leaves(34)
#print(ajay.leaves)

print(kani.salary)

