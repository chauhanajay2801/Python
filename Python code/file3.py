f = open("ajay2.txt")
print(f.tell())#tell about the pointer loction
print(f.readline())
f.seek(0)# to tell the pointer where to go
print(f.tell())
print(f.readline())
f.close()