import random
from itertools import repeat
from functools import partial
from operator import methodcaller


def call_n_times(tim):
    clock = 0
    got = ""
    while (clock - tim) != 0:
        form = [str(random.randint(0, 9)), random.choice(abc).upper(), random.choice(abc)]
        clock += 1
        got += random.choice(form)
    else:
        return got


abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
isEnd = False

while True and not isEnd:
    usnput = input("How many characters long do you want your password to be? : ")
    while usnput.isdigit():
        if int(usnput) > 4 and int(usnput) < 21:
            pwd = call_n_times(int(usnput))
            print("Here is your password ---->  " + pwd)
            isEnd = True
            break
        else:
            print("Sorry! The password must be between 5 and 20 characters long")
            break
    if not usnput.isdigit() and not isEnd:
        print("Please, enter a number")