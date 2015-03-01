'''
A function that adds two ints together.
'''

def add_ints(int1, int2):
    if isinstance(int1, int) and isinstance(int2, int):
        return int1 + int2
    else:
        raise TypeError

    
    