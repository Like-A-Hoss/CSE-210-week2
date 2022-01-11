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
        """Rolls 5d6 and puts resulsts in list"""
        counter =1
        while counter <=5:
            d6 = die()
            d6.roll()
            self.rolls.append(d6.see_roll())
    def get_rolls(self):
        """displays results of rolls as a print command"""
        print(f"[{self.rolls[0]}] [{self.rolls[1]}] [{self.rolls[2]}] [{self.rolls[3]}] [{self.rolls[4]}]")

class player():
    def __init__(self) -> None:
        """sets up a player"""
        self.player_name = "Player 1"
        self.score = 0
    def set_score(self, points):
        """sets the score by adding the points passed in."""
        self.score += points

class player():
    def __init__(self) -> None:
        """sets up a player"""
        self.player_name = "Player 1"
        self.score = 0
    def set_score(self, points):
        """sets the score by adding the points passed in."""
        self.score += points

def main():
    new_player = player()
    play = True
    print(f"Welcome New Player your current score is {new_player.score}")
    while play == True:
        the_dice = dice()
        the_dice.set_rolls()
        the_dice.get_rolls()
        points = 0
        for num in the_dice:
            if num == 1:
                points += 100
            elif num == 5:
                points += 50
        if points == 0:
            print(f"GAME OVER!  You ended the game with {new_player.score} Points better luck next time.")
            play = False
        else:    
            player.set_score(points)
            print(f"{new_player.player_name} your score is {new_player.score}")
            keep_Playing = input("Roll the dice? Y/N")
            if keep_Playing.upper == "N":
                play = False
                print(f"Disgression is the better part of valor.  Your score was {new_player.score}.")
            else:
                print("rolling")
#New let's Boogey
if __name__ == "__main__":
    main()
