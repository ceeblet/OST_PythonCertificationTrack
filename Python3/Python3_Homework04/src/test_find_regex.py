'''
Created on Nov 20, 2014

@author: cbrown
'''
import unittest
from find_regex import find_position

class Test(unittest.TestCase):


    def testFindRegex(self):
        self.text = """In the 1950s, mathematician Stephen Cole Kleene described automata theory and formal language theory in a set of models using a notation called "regular sets" as a method to do pattern matching. Active usage of this system, called Regular Expressions, started in the 1960s and continued under such pioneers as David J. Farber, Ralph E. Griswold, Ivan P. Polonsky, Ken Thompson, and Henry Spencer."""
        self.assertTupleEqual(find_position("Regular Expressions", self.text), (231, 250))
        self.assertIsNone(find_position("RegularExpression", self.text))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFindRegex']
    unittest.main()