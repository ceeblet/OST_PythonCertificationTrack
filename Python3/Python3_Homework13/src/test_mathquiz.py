import unittest
import mathquiz

class TestMathQuiz(unittest.TestCase):
    
    def test_add_two_nums(self):
        self.assertEqual(mathquiz.add_two_nums(3,5), 8)
    
    def test_calculate_average_time(self):
        self.assertEqual(mathquiz.calculate_average_time([1,2,3,4,5]), 3.0)
    
if __name__ == "__main__":
    unittest.main()
    
