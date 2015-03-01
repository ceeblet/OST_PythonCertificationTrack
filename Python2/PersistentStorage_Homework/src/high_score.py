"""
Write a function (not a class) that takes two arguments, 
a string player name and an integer score, and keeps a 
"high score" table in a Python shelve. If the integer 
argument is higher than the given player's current 
high score (or if the player has no recorded high score), 
log the value as this player's new high score. 
The function should return the player's current high score. 
Remember, a function is not the same thing as a class and 
it's a function that's needed.
"""

import shelve

scoreShelf = r'highScore.shlf'

def high_score(name, score):

    score_shelf = shelve.open(scoreShelf, writeback=True)

    if name not in score_shelf:
        score_shelf[name] = score
    elif score_shelf[name] < score:
        score_shelf[name] = score
    highest = score_shelf[name]
    score_shelf.close()
    return highest

