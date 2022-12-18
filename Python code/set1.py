it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
it2 = {'Xebia','Meta','Netflix'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Tweeter")
print(it_companies)

it_companies.update(it2)
print(it_companies)

it_companies.pop()
print(it_companies)
it_companies.discard("IB")
print(it_companies)
it_companies.remove("IBM")
print(it_companies)

