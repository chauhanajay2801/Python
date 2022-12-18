def pallin(number):
    rever = 0
    a = number
    while (a>0):
        rever = rever*10+a%10
        a = a//10

    if rever == number:
        print("psllin")
    else:
        print("not a pallindrome")





number = int(input("Enter ur number"))
pallin(number)