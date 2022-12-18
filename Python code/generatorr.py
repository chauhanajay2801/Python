def gen(n):
    for i in range(n):
        yield i

a = gen(6)
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())


b = "Ajay" # this is iterable means it have iter method defined
for d in b:
    print(d)

e = iter(b)
print(e.__next__())