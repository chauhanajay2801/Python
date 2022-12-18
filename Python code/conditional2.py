"""a = int(input("What are ur scores?"))

if a>=80:
    print("Your grade is A")
elif a>=70 and a<=79:
    print("Your grade is B")
elif a>=60 and a<=69:
    print("Your grade is C")
elif a>=50 and a<=59:
    print("Your grade is D")
elif a<=49:
    print("Your grade is F")



fruits = ['banana','orange','mango']
a = input("enter the fruit")
if a in fruits:
    print("we already have this fruit in the database")
else:
    fruits.append(a)
    print(fruits)
"""
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'}}
#if 'skills' in person:
#    print(person['skills'][3])
if 'skills' in person:
    if 'python' in person['skills']:
        print("Yes the person have python in skills")
    