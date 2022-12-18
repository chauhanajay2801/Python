a = open("ajay.txt")
#content = a.read()
#print(content)
print(a.readlines()) # put it in a list line by line and then display
#print(a.readline()) # to read line by line

#for line in a:
#    print(line,end="")
a.close() #to freeup the allocated resources

