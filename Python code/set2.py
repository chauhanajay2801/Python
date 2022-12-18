it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it2 = {'Xebia','Meta','Netflix'}
sent = "I am a teacher and I love to inspire and teach people"
A = {19, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

A.update(B)
print(A)

print(A.intersection(B))

print(A.issubset(B))

print(B.isdisjoint(A))

B.union(A)
print(B)

A.clear()
print(A)

age = set(age)
print(age)


sen = sent.split()
print(sen)
sen = set(sen)
print(sen)
