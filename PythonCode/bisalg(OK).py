
import random
from math import trunc

lst = (random.sample(range(100), 50))
num = .1

random.shuffle(lst)
while not isinstance(num, int) and num <= 99:
    try:
        num = int(input("Enter a number between 0 and 99 in order to search it on a 50 random numbers list: "))
    except ValueError as ve:
        print("ERROR INVALID NUMBER")
    continue
print(str(lst) + "      ('''Pre-while binary search loop''')")
while len(lst) != 2:
    length = len(lst)
    mid = trunc(length/2)
    if num in lst[mid+1:]:
        del lst[:mid]
        print(str(lst) + "      -> (if num in lst[mid+1:] <-")
    elif num in lst[:mid]:
        del lst[mid+1:]
        print(str(lst) + "      -> (elif num in lst[:mid] <-")
    else:
        del lst[:mid]
        print(str(lst) + "      -> (else) <- (Number is not on the list so del lst[:mid]")
    continue
print(str(lst) + "      ('''Post-while binary search loop''')")
if num == lst[0]:
    del lst[1]
    print("Your number was on the list!")
    print("(Here is the list that results from the binary search) -> del lst[1] <-      " + str(lst))
elif num == lst[1]:
    del lst[0]
    print("Your number was on the list!")
    print("(Here is the list that results from the binary search) -> del lst[0] <-      " + str(lst))
else:
    del lst[0:]
    print("Your number wasn't on the list :(")
    print("(Here is the list that results from the binary search)   " + str(lst))
