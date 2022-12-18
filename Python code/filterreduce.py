list1 = [1,2,5,9,6,4]

def is_greater(num):
    return num>5

print(is_greater(10))

greater = list(filter(is_greater, list1))
print(greater)



#reduce

from functools import reduce

lis = [1,2,3,4]
a = reduce(lambda x,y:x+y,lis)
print(a)