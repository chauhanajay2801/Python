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

class Player:
    no_of_games = 4

    def __init__(self,name,game):
        self.name = name 
        self.game = game

    def printdetails(self):
        return f"name is {self.name} and game is {self.game}"

class CoolProgrammer(Employee,Player):
    language ="c++"
    
    def printl(self):
        return f"name is {self.name} and language is {self.language}"





shubham = Player("Shubham", ["Cricket"])
Rashmi = CoolProgrammer("Rashii", 12000000, "Coolcoder")
print(Rashmi.printdetails())
print(Rashmi.printl())