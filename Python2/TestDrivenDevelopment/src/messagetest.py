"""
Demonstrate a message formulated by the unittest syste.
"""

import unittest

class DemoCase(unittest.TestCase):
    def testMessage1(self):
        self.assertEqual([1,2,3,4], [1, 2, [3, 4]])
        
if __name__ == "__main__":
    unittest.main()