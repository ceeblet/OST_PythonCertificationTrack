#!/usr/local/bin/python3
""" doggies.py """

import sys

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def __str__(self):
        return "%s: %s" % (self.name, self.breed)
    

if __name__ == "__main__":
    dogs = []

    while True:
        inputtext = "Name: "
        inputtext2 = "Breed: "
    
        inp1 = input(inputtext)
        if inp1:
            inp2 = input(inputtext2)
        else:
            sys.exit()
        
        if inp1:
            mydog = Dog(inp1, inp2)
            dogs.append(mydog)
            print("DOGS")
            for i, dog in enumerate(dogs):
                print("{0}. {1}".format(i ,dog))    
            print("*" * 40)
        