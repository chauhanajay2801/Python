"""
import string
import random

def get_random():
    letters = string.ascii_letters
    lett = string.digits
    result_str = ''.join(random.choice(lett) for i in range(6))
    print("Random string of length", "is:", result_str)

get_random()
"""
import random
import string

def get_ran():
    a = range(255)
    resullt = (random.choice(a) for i in range(3))
    print(resullt)

get_ran()