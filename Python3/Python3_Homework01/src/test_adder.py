'''
Created on Nov 15, 2014

@author: cbrown
'''
import unittest
from adder import add_ints


class Test(unittest.TestCase):

    def test_adder_errors(self):
        #self.assertRaises(TypeError, add_ints("string1", "string2"))
        #self.assertRaises(TypeError, add_ints(1, "string2"))
        #self.assertRaises(TypeError, add_ints(1.4, 3))
        self.assertRaises(TypeError, add_ints, "string1", "string2")
        self.assertRaises(TypeError, add_ints, 1, "string2")
        self.assertRaises(TypeError, add_ints, 1.4, 3)
        
    def test_adder_successes(self):
        self.assertEqual(add_ints(1, 5), 6)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_adder']
    unittest.main()