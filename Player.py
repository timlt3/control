from Card import Card
import Game
import operator  #FOR SORTING HANDS, lets you sort on class members
from Constants import *
from Util import *

class Player(): 
    def __init__(self, name):
        self.hand = [] 
        self.tab = []
        self.name = name

    #SORT HANDS 
    #works by sorting list by card value i.e. WORKS FOR TABLEAUS
    def sortHandAndTableau(self): 
        self.hand = sorted(self.hand, key=operator.attrgetter('value'))
        self.tab = sorted(self.tab, key=operator.attrgetter('value'))

    #DRAW CARD
    def draw(self): 
        self.sortHandAndTableau()
        # TODO: Should we assume here that the player has less than 7 cards?
        if len(Game.getGame().deck) != 0 and len(self.hand) < HAND_LIMIT:
            self.hand.append(Game.getGame().deck.pop(0))

    #GET SCORE
    def getScore(self): 
        self.sortHandAndTableau()
        score = 0
        for x in self.tab:
            score += x.value
        return score

    #PRINT HAND 
    def printHand(self): 
        self.sortHandAndTableau()
        prettyPrintCards(self.hand)

    #PRINT TAB 
    def printTab(self): 
        self.sortHandAndTableau()
        print("\n")
        print(self.name, "'s score is: ", self.getScore())
        print(self.name, "'s Tableau is: ") 
        print("======================")
        prettyPrintCards(self.tab)
        print("======================")

