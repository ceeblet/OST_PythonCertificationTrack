import unittest
from furnishings import *

class TestFurnishings(unittest.TestCase):
    
    def setUp(self):
        self.home = []
        self.home.append(Bed('Bedroom'))
        self.home.append(Sofa('Living Room'))
        self.home.append(Table('Bedroom'))
        self.home_map = map_the_home(self.home)
        
    def test_map_the_home(self):
        self.assertEqual(2, len(self.home_map))
        self.assertEqual(2, len(self.home_map['Bedroom']))
        self.assertEqual(1, len(self.home_map['Living Room']))
        
#    def test_counter(self):
#        counter(self.home)
                
if __name__ == '__main__':
    unittest.main()