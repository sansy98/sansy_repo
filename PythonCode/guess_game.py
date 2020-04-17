from random import randint

rannum = str(randint(1, 20))
guess = ""
tries_left = 10
zero_tries = False

while guess != rannum and not zero_tries:
    guess = input("Guess a number from 1 to 20: ")
    tries_left -= 1
    if tries_left == 0:
        zero_tries = True
    elif guess != rannum and not zero_tries:
        print("Wrong number!\nYou have " + str(tries_left) + " attempts left.")


if zero_tries:
    print("Out of tries!!")
else:
    print("That's correct, you've won!!!!")
