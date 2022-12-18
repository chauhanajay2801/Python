class Employee:
    leaves = 10
    def __init__(sel,aname,asalary,arole): #constructor it takes argument and initialize automatically
        sel.name = aname
        sel.salary = asalary
        sel.role = arole

    
    def printdetails(sel):
        return f"name is {sel.name} and Salary is {sel.salary} and role is {sel.role}"

ajay = Employee("Ajay Chauhan",200000,"Data Engineer") #instance of class

# to give argument in one go we need constructor

#ajay.name = "Ajay Chauhan"
#ajay.salary = 200000
#ajay.role = "Data Engineer"

#rahul.name = "Rahul Dangwal"
#rahul.salary = 100000
#rahul.role = "Node.js"

print(ajay.printdetails())