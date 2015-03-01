""" title_test.py - testing the title function. """
import unittest

def title(s):
    "How close is this function to str.title()?"
    #return s[0].upper()+s[1:]
    news = s.split()
    finalString = ""
    for word in news:
        finalString += word.title() + " "
    return finalString.strip()

class TestTitle(unittest.TestCase):
    def test_all_upper(self):
        s = "THIS IS ALL CAPS."
        self.assertEqual(title(s), s.title(), "All caps does not work.")

    def test_all_lower(self):
        s = "this is all lower case."
        self.assertEqual(title(s), s.title(), "all lower case does not work.")
        
    def test_mixed(self):
        self.assertEqual(title("this Is MIXED cAsE."), "this Is MIXED cAsE.".title(), "mixed case does not work.")
  
    def test_real_book_and_movie_titles(self):
        for s in ["war and peace", " 2001:  space  Odyssey", "the avengers"]:
            self.assertEqual(title(s), s.title(), "Outcomes not the same")
            
#    def test_title(self):
#        switch = [
#            "THIS IS ALL CAPS.",
#            "this is all lower case.", 
#            "this Is MIXED cAsE."       
#        ]
#        for s in switch:
#            print(s)
#            self.assertEqual(title(s), s.title(), s)
      
if __name__ == "__main__":
    unittest.main()