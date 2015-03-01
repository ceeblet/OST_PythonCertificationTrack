#!/usr/local/bin/python3
"""Guessing game. Verifies a number input by a user with a secret number."""

attempts = 0
tries = 5
secret = 12

guess = int(input("Guess a number between 1 and 20 (you have 5 tries): "))
while attempts < (tries - 1):
    attempts += 1
    if guess == secret:
        print("Correct! Well done, the number was ", secret)
        break
    elif guess < secret:
        print("You need to guess higher.")
    elif guess > secret:
        print("You need to guess lower.")   
    print("You have ", tries - attempts, " guess(es) left in the game.") # guess(es) is lazy
    guess = int(input("Guess again: "))
if guess != secret:
    print("So sorry, you lose. Better Luck next time.")
