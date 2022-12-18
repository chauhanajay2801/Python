"""a = open("ajay1.txt","w")
b = a.write("bhaiya main bhaiya ajay bhaiya\n")
print(b)
a.close()"""

#handle read and write both
a = open("ajay2.txt","r+")
print(a.read())
b = a.write("kati jeher")

a.close()

