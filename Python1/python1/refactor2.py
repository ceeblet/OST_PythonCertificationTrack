#!/usr/local/bin/python3
""" Refactored version of previous example. """

def list_multiply(a, b):
    """ Sums two lists of integers and multiplies them together
    
    >>> list_multiply([3,4],[3,4])
    49
    >>> list_multiply([1,2,3,4],[10,20])
    300
    """
    
    return sum(a) * sum(b)
    
def _test():
    import doctest, refactor
    return doctest.testmod(refactor)
    
if __name__ == "__main__":
    _test()
    