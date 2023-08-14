#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from Board import Board

# write your class below.

class Player:
    
    def __init__(self, checker):
        """ constructor that constructs a new Player object by initializing the following 
        two attributes:"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        checker = Player
        self.num_moves = 0
        
    def  __repr__(self):
        """ method that returns a string representing a Player object. The string 
        returned should indicate which checker the Player object is using"""
        if self.checker == 'X':
            return 'Player X'
        elif self.checker == 'O':
            return 'Player O'

    def opponent_checker(self):
        """ method that returns a one-character string representing the checker of the
        Player object’s opponent. The method may assume that the calling Player object 
        has a checker attribute that is either 'X' or 'O'."""
        if self.checker == 'X':
            return 'O'
        elif self.checker == 'O':
            return 'X'
    
    def next_move(self, b):
        """  method that accepts a Board object b as a parameter and returns the column
        where the player wants to make the next move. To do this, the method should ask 
        the user to enter a column number that represents where the user wants to place 
        a checker on the board."""
        x = int(input('Enter a column: '))
        while x < 0 or x > range(b.width)[-1]:
            print('Try again')
            x = int(input('Enter a column: '))
        else:
            self.num_moves += 1
            return x

        
        
        