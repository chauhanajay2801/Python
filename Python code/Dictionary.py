dog  = {}
dog["name"] = "bruno"
dog["color"] = "brown"
dog["breed"] = "bulldog"
dog["legs"] = 4
dog["name"] = 10

student = {"first_name":"Ajay","last_name":"Chauhan","gender":"Male",
"age":19,"marital status":"Taken","skills":["python","html","css","javascript"],
"country":"India","city":"faridabad","address":{"1768","jawahar colony","nit faridabad"}}
student["skills"].append("django")
print(student["skills"])
ky = student.keys()
print(ky)
vl = student.values()
print(vl)
student=student.items()
print(student)

del dog
print(dog)