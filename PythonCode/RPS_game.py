
from random import choice

options = ["R", "P", "S"]

pychoice = choice(options)
uschoice = ""
good = ""
ongoing = True
draw = False
win = False


uschoice = input("Rock(R) Paper(P) or Scissors(S)?: ").upper()
if uschoice in options:
    if pychoice == options[0]:
        good = options[1]
    elif pychoice == options[1]:
        good = options[2]
    else:
        good = options[0]

    while ongoing:
        print("Your opponent chose: " + pychoice)
        if pychoice == uschoice:
            draw = True
            ongoing = False
        elif uschoice == good:
            win = True
            ongoing = False
        else:
            ongoing = False

    if draw:
        print("It's a draw!")
    elif win:
        print("You've won!")
    else:
        print("You've lost!")

else:
    print("ERR0R! Invalid input!!")
