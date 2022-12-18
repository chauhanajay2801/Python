a = "Thirty"
b = "days"
c = "of"
d = "python"
space = " "
print(a + space + b + space + c + space + d)

company = "Coding for All"
faang = "meta,google,apple,ibm"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:6])
print(company.find("Coding"))
print(company.replace("All","Everyone"))
print(company.replace("Coding for All", "Python"))
print(company.split())
print(company[0])
print(company[-1])
print(faang.split(','))
print(company[0::4])
print(company.index("o"))
print(company.rindex("o"))
print(company.startswith("Coding"))
print(company.endswith("coding"))

st = "you cannot end a sentence with because because because is a conjunction"
print(st.index("because"))
print(st[31:38],st[39:47])

lib = ['Django','flask','pyramid']
print('# '.join(lib))