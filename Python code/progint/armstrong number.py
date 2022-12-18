a = int(input("Enter ur number"))
orig = a
sum = 0

while (a>0):
    sum = sum + (a%10)**3
    a = a//10

if orig == sum:
    print("Yes")
else:
    print("No")