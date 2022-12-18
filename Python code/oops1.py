class Employee:
    no_of_leaves = 8 #class variable

ajay = Employee() #instance of class
rahul = Employee()

ajay.name = "Ajay Chauhan"
ajay.salary = 200000
ajay.role = "Data Engineer"

rahul.name = "Rahul Dangwal"
rahul.salary = 100000
rahul.role = "Node.js"

print(Employee.no_of_leaves)
ajay.no_of_leaves = 15
print(ajay.__dict__)# return a dictionary contains information of a object of class


print(Employee.no_of_leaves)

Employee.no_of_leaves = 12
print(rahul.no_of_leaves)

