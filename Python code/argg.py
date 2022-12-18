
def arggs(*args,**kwargs):
    print(args[0])
    for i in args:
        print(i)
    print("\n Now some of our special mention")
    for key,value in kwargs.items():
        print(f"{key} is a {value}")

name = ["ajay","rajat","aviral"]
role = {"Ajay":"Python programmer","Ramesh":"sweeper","Amit":"sarkari naukar"}
arggs(*name,**role)