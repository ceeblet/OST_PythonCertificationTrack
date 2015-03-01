#!/usr/local/bin/python3
"""Guessing game. Verifies a number input by a user with a secret number."""

attempts = 0
tries = 5
secret = 12

guess = int(input("Guess a number (you have 5 tries): "))
while True:
    attempts += 1
    if guess == secret:
        print("Correct! Well done, the number was ", secret)
        break
    elif guess < secret:
        print("You need to guess higher.")
    elif guess > secret:
        print("You need to guess lower.")
    print("You have ", tries - attempts, " left in the game.")
    if attempts == tries:
    	print("So sorry, you lose. Better Luck next time.")
    	break
    guess = int(input("Guess again: "))
