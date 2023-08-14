#
# ps9pr4.py (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four  
#

import random  
from Connect_Four import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructor that constructs a new AIPlayer object. """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead
    
    def __repr__(self):
        """ method that returns a string representing an AIPlayer object. This method 
        will override/replace the __repr__ method that is inherited from Player. """
        x = ''
        z = ' '
        if self.checker == 'X': 
            x += ('Player X' + z + '(' + str(self.tiebreak) + ',' + z + str(self.lookahead) \
                  + ')')
            return x
        elif self.checker == 'O':
            x += ('Player O' + z + '(' + str(self.tiebreak) + ',' + z + str(self.lookahead) \
                  + ')')
            return x
        
    def max_score_column(self, scores):
        """ method that takes a list scores containing a score for each column of the 
        board, and that returns the index of the column with the maximum score. If one 
        or more columns are tied for the maximum score, the method should apply the 
        called AIPlayer‘s tiebreaking strategy to break the tie. """
        x = max(scores)
        listof = []
        for i in range(len(scores)):
            if scores[i] == x:
                listof += [i]
        if self.tiebreak == 'LEFT':
            return listof[0]
        elif self.tiebreak == 'RIGHT':
            return listof[-1]
        else:
            return random.choice(listof)
        
    def scores_for(self, b):
        """ method that takes a Board object b and determines the called AIPlayer‘s 
        scores for the columns in b. """ 
        score = [100] * b.width
        for col in range(b.width):
            if b.can_add_to(col) == False:
                score[col] = -1
            elif b.is_win_for(self.checker) == True:
                score[col] = 100
            elif b.is_win_for(self.opponent_checker()) == True:
                score[col] = 0
            elif self.lookahead == 0:
                score[col] = 50
            else:
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead \
                                    - 1)
                opponent_score = opponent.scores_for(b)
                if 100 == max(opponent_score):
                    score[col] = 0
                elif 0 == max(opponent_score):
                    score[col] = 100
                elif 50 == max(opponent_score):
                    score[col] = 50
                b.remove_checker(col)
                
        return score
                          
    def next_move(self, b):
        """ method that overrides (i.e., replaces) the next_move method that is inherited 
        from Player. Rather than asking the user for the next move, this version of 
        next_move should return the called AIPlayer‘s judgment of its best possible move."""
        x = self.scores_for(b)
        return self.max_score_column(x)
            