
import random
from itertools import repeat
from functools import partial
from operator import methodcaller


def call_n_times(function):
    clock = 0
    got = ""
    while clock != usnput:
        clock = clock + 1
        got = got + function
    else:
        return got


abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
form = [str(random.randint(0, 9)), random.choice(abc).upper(), random.choice(abc)]


usnput = input("How many characters long do you want your password to be? : ")

while usnput.isdigit():
    if int(usnput) >= 5 <= 20:
        pwd = call_n_times(random.choice(form))
        print("Here is your password ---->  " + pwd)
    else:
        print("Sorry! The password must be between 5 and 20 characters long")
else:
    print("Please, enter a number")
    continue

