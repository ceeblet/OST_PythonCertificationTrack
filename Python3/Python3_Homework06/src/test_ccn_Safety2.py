'''
Created on Nov 21, 2014

@author: cbrown
'''
import unittest
from ccn_safety2 import redact_cc

class Test(unittest.TestCase):


    def testCcnRedaction(self):
        testText = """Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or 5555-5555-5555-5555? It is because a number that appears to be real, such as 1234-5678-1234-5678, triggers the attention of privacy and security experts."""
        expectedText = """Have you ever noticed, in television and movies, that phone numbers and credit cards are obviously fake numbers like 555-123-4567 or CCN REMOVED FOR YOUR SAFETY? It is because a number that appears to be real, such as CCN REMOVED FOR YOUR SAFETY, triggers the attention of privacy and security experts."""

        self.assertEqual(redact_cc(testText), expectedText)
    
    def testCcnRedationNoCCn(self):
        testText = "Return text unchanged if there are no credit card numbers."
        
        self.assertEqual(redact_cc(testText), testText)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCcnSafety']
    unittest.main()