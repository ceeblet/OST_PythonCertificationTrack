import unittest
import os
import glob
from high_score import high_score

class TestHighScore(unittest.TestCase):
    
    def tearDown(self):
        for f in glob.glob("highScore.shlf.*"):
            os.remove(f)
    
    def testGetPlayersHighScore(self):
        player1 = "TestPlayer One"
        player1Score = 289
        self.assertEqual(high_score(player1, player1Score), player1Score, "player score returned not equal to TestPlayer")
    
    def testHigherScore(self):
        player2 = "TestPlayer Two"
        player2Score = 200
        high_score(player2, player2Score)
        player2HigherScore = 300
        self.assertEqual(high_score(player2, player2HigherScore), player2HigherScore, "player two higher score not equal")
        
    def testNoRecordedScore(self):
        pass
    
    def testLowerScore(self):
        player3 = "TestPlayer Three"
        player3Score = 100
        high_score(player3, player3Score)
        player3LowerScore = 80
        self.assertEqual(high_score(player3, player3LowerScore), player3Score, "player three highest score not equal" )
        
    def testStoreHighScore(self):
        HighScore = high_score
        self.assertEqual(-100, HighScore('joe', -100))
        self.assertGreater(-99, HighScore('joe', -100))
        self.assertEqual(0, HighScore('joe', 0))
        self.assertLess(0, HighScore('chris', 100))
        self.assertEqual(1000, HighScore('chris', 1000))
        self.assertLess(100, HighScore('chris', 1000))
        
    def test_many_scores(self):
        HighScore = high_score
        self.assertEqual(50, HighScore('Kirby', 50))
        self.assertEqual(150, HighScore('Kirby', 150))
        self.assertEqual(150, HighScore('Kirby', 40))
        self.assertEqual(150, HighScore('Kirby', 95))
        self.assertTrue(HighScore('Kirby', 180) == 180, 'Kirby should have 180 as a top score')
        
if __name__ == "__main__":
    unittest.main()