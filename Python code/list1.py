a = []
b = ["b","r","p","q","l","o"]
print(len(b))
print(b[0],b[2],b[5])

person = ["Ajay Chauhan","27","5'7","taken","1768,jawahar colony"]
print(person)

it_companies = ["facebook","google","microsoft","apple","ibm","oracle","amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0::3])
it_companies[2] = "tcs"
print(it_companies)
it_companies[3] = "yamaha"
print(it_companies)
it_companies.append("#")
print(it_companies)
ex = "google" in it_companies
print(ex)
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
it_companies.clear()
print(it_companies)

fe = ["q","w","e"]
qe = ["r","t","y","i"]
fe.extend(qe)
print(fe)
ty = fe.copy()
print(ty)