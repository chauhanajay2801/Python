class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    def explain(self):
        
        return f"This employee is {self.fname} {self.lname}"

    @property#property dectorator
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@codewithajay.com"


    @email.setter #setter dunction help to set some value 
    def email(self,str):
        print("setting now")
        names = str.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter #used to delete the created setter ,in oop programming we make it none insted od deleting
    def email(self):
        print("Deleting now")
        self.fname = None
        self.lname = None


nikhil = Employee("Nikka","Jaildaar")
raj = Employee("Raj","Kumar")

print(Employee.explain(nikhil))
nikhil.fname = "Nikita"
print(nikhil.email)
nikhil.email= "Ajay.chauhan@codewithajay.com"
print(nikhil.fname,nikhil.lname)

del nikhil.email
print(nikhil.email)