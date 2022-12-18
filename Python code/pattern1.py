a = int(input("enter row numbers"))
b = input("Enter 0 or 1")

if b ==0:
    for i in range(a):
        print("*"*i)
else:
    for i in range(a,0,-1):
        print("*"*i)
