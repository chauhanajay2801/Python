# sum of all divisor exclusing that number

sum = 0
n = int(input("Enter a number"))
for i in range(1,n):
    if n%i==0:
        sum = sum+i
if sum == n:
        print("Perfect")
else:
        print("not perfect")