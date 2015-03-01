#!/usr/local/bin/python3
""" Demonstrates an opportunity for refactoring. """

def list_multiply(LIST_A, LIST_B):
    """ Sums two lists of integers and multiplies them together
    
    >>> list_multiply([3,4],[3,4])
    49
    >>> list_multiply([1,2,3,4],[10,20])
    300
    """
    
    TOTAL_A = 0
    for i in LIST_A:
        TOTAL_A += i
    TOTAL_B = 0
    counter = 0
    while True:
        if counter > len(LIST_B) - 1:
            break
        TOTAL_B = TOTAL_B + LIST_B[counter]
        counter += 1
    return TOTAL_A * TOTAL_B
    
def _test():
    import doctest, refactor
    return doctest.testmod(refactor)
    
if __name__ == "__main__":
    _test()
    