"""def add_two_numbers(x,y):
    z = x+y
    print(z)


add_two_numbers(10, 20)


def area_circle(x):
    y = 3.14*x*x
    print(y)

area_circle(5)

def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num,(int)):
            total = total + num
        else:
            print("It is not a number")
    print("This is the ",total)

print(add_all_nums(3,4,5,"qw"))

def c_f(n):
    change = (n*9/5)+32
    print(change) 

c_f(10)




def print_list(a):
    for i in a:
        print(i)

a = [1,2,3,4,5]
print_list(a)



def rever(a):
    b =[]
    for i in range(len(a)):
        c=a.pop()
        b.insert(i,c)
    return b

a = [1,2,3,4,5]
print(rever(a))



def capitalize_list_items(a):
    b = []
    for i in a:
        b.append(i.upper())
    return b

    c =[j.upper() for j in a]
    return c


a =['ajay','pritam']
print(capitalize_list_items(a))


def add_item(food_staff,a):
    food_staff.append(a)
    return food_staff

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
#numbers = [2, 3, 7, 9];
#print(add_item(numbers, 5))      [2, 3, 7, 9, 5]


def remove_item(a,b):
    for i in a:
        if i == b:
            a.remove(i)
    return a

a = [2, 3, 7, 9]
print(remove_item(a, 3))  # [2, 7, 9]


def add(a):
    b = 0
    for i in range(a+1):
        b = b+i
    print(b) 

add(50)
"""


























