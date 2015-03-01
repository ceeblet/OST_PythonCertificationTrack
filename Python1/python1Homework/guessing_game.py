#!/usr/local/bin/python3
""" guessing_game.py """

import random
#print(help(random))
rnum = random.randint(1,99)

while True:
    input_string = "Guess a number: "
    unum = input(input_string)
    if int(unum) == rnum:
        break
    if int(unum) < rnum:
        print("Too low")
    if int(unum) > rnum:
        print("Too high")
print("You guessed it!")
