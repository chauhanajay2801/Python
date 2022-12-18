#using with to open the file it wont need file close

with open("ajay2.txt") as f:
    a = f.read(4)
    print(a)