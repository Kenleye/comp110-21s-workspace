"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730316492"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
magic_number: int = randint(1,11)
if magic_number < 2: 
    print("you will get an A in COMP110")
else: 
    if magic_number < 4:
        print("you will fail COMP110")
    else:
        if magic_number < 6:
            print("you are amazing and your COMP110 grade doesn't define you")
        else: 
            if magic_number < 8:
                print("you are so good at COMP110 you will be the next Kris Jordan")
            else:
                print("you should stick to being a psych major")

if magic_number == 10:
    print("jackpot! you have 110 years of good luck.")
    