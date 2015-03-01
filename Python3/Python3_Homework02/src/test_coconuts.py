'''
Created on Nov 17, 2014

@author: cbrown
'''
import unittest
import coconuts


class Test(unittest.TestCase):
    #def setUp(self):
        #self.coconutInventory = coconuts.Inventory()
        
    def testTypeWeightsDifferent(self):
        #self.assertFalse(self.saCoconut.weight == self.meCoconut.weight, "South Asian and Middle Eastern coconuts have the same weight.")
        self.assertFalse(coconuts.SouthAsian().weight == coconuts.MiddleEastern().weight, "South Asian and Middle Eastern coconuts have the same weight.")
        self.assertFalse(coconuts.American().weight == coconuts.MiddleEastern().weight, "American and MiddleEastern coconuts have the same weight.")
        self.assertFalse(coconuts.SouthAsian().weight == coconuts.American().weight, "South Asian and American coconuts have the same weight.")
        
    def testStringAttributeError(self):
        self.coconutInventory = coconuts.Inventory()
        self.assertRaises(AttributeError, self.coconutInventory.add_coconut, "coconut")
    
    def testAddedTotalWeight(self):
        self.coconutInventory = coconuts.Inventory()
        self.expected = 19
        self.coconutInventory.add_coconut(coconuts.SouthAsian())
        self.coconutInventory.add_coconut(coconuts.SouthAsian())
        self.coconutInventory.add_coconut(coconuts.MiddleEastern())
        self.coconutInventory.add_coconut(coconuts.American())
        self.coconutInventory.add_coconut(coconuts.American())
        self.coconutInventory.add_coconut(coconuts.American())

        self.assertEqual(self.coconutInventory.total_weight(), self.expected)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCoconuts']
    unittest.main()