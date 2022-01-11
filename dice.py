'''This program will roll 5d6 and check for 5's and 1's mark them for points.  100 for each 1 and 50 for each 5.
The game will continue until the player opts to stop, allowing them to back out when ever they choose.  With a minor win
The game will continue until player rolls no successes.'''
from random import  randint as roller
class die():
    '''A dice object that will roll a dice, and return an outcome'''
    def __init__(self) -> None:
        self.sides = 6
        self.roll_results = 0
    def roll(self):
        '''the roller that will take the sides and roduce the outcome.  this function sets roll results'''
        self.roll_results = roller(1,self.sides)
    def see_roll(self):
        """this passes out the results of the roll"""
        return self.roll_results

class dice():
    def __init__(self) -> None:
        self.rolls =[]
    def set_rolls(self):
        counter =1
        while counter <=5:
            d6 = die()
            d6.roll()
            self.rolls.append(d6.see_roll())
        