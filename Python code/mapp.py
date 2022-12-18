number = ["1","2","3","4"]
numbers = list(map(int,number))
print(numbers)

numbu = [1,2,3,4,5]
square = list(map(lambda x:x*x, numbu))
print(square)


def square(a):
    return a*a

def cube(a):
    return a*a*a

func=[square,cube]

for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)