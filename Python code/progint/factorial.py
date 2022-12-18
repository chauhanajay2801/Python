def fact(n):
    if n == 0:
        return 1
    
    return n*fact(n-1)


"""fac = 1
for i in range(5):
    fac = fac*(i+1)
print(fac)"""

a = int(input("Enter the number"))
result = fact(a)
print(result)

    