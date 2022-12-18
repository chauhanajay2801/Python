"""
def find(a):
    b =0
    c =0
    for o in range(a+1):
        if o%2==0:
            b = b+1
        else:
            c = c+1
    print("the number of even numbers are",b,"the number of odd nos are",c)

find(100)


def factorial(a):
    fact = 1
    for i in range (1,a+1):
        fact = fact*i
    print(fact) 

factorial(4)
"""

def check(a):
    if len(a) == 0:
        print('it is empty')

check(1)