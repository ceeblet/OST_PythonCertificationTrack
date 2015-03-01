#!/usr/local/bin/python3
"""Guessing game. Generates a psudo-random number between 1 and 20 and gives a user five tries to guess what it is."""

import random

tries = 5
secret = random.randint(0, 21)
guess = int(input("Guess a number between 1 and 20 (you have 5 tries): "))
attempts = 1
while attempts < tries:
    if guess == secret:
        print("Correct! Well done, the number was ", secret)
        break
    elif guess < secret:
        print("You need to guess higher.")
    elif guess > secret:
        print("You need to guess lower.")   
    print("You have ", tries - attempts, " guess(es) left in the game.")
    guess = int(input("Guess again: "))
    attempts += 1
if guess == secret and attempts == tries:
    print("Correct! Well done, the number was ", secret, ". You got it just in time!")
elif guess != secret:
    print("So sorry, you lose. Better Luck next time.")