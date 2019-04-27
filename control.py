from enum import Enum
import csv #for reading csv file 
from random import shuffle #for shuffling the deck
import operator  #FOR SORTING HANDS, lets you sort on class members

STARTING_HAND_SIZE = 5
HAND_LIMIT = 7

class CardName(Enum):
    RIFT = 1
    EXOTIC_MATTER = 2
    DEFLECTOR = 3
    WORMHOLE = 4
    ANOMALY = 5
    REWIND = 6
    REACTOR = 7
    DARK_ENERGY = 8
    FUTURE_SHIFT = 9
    SINGULARITY = 10
    ANTIMATTER = 11
    TIME_STOP = 12
    NOVA = 13

class Card(): 
    def __init__(self, name, value, color, description):
        self.name = name.strip()
        self.value = int(value)
        self.color = color.strip()
        self.description = description.strip()

        # Access enum with spaces replaced with _
        n =  self.name.replace(" ", "_") 
        self.ID = CardName[n]
    
    def __repr__(self): 
        return "Card()" 

    #allows print() to correctly handle Card class 
    def __str__(self): 
        seq ="%13s %2d %s %s" % (str(self.name) ,self.value , str(self.color) , str(self.description))
        return seq

    def onInstall(self):
        print(self.name + ": Install effects not implemented")
        #if self.ID == CardName.RIFT:
        #RIFT DESTROYS A NOVA OR ALLOWS USER TO DRAW CARD
        #elif self.ID == CardName.EXOTIC_MATTER:
        #CHAIN CELLS WITH 6 OR LESS CHARGE

    def onDiscard(self):
        print(self.name + ": Discard effects not implemented")
        #if self.ID == CardName.WORMHOLE:
        #elif self.ID == CardName.ANOMALY:
        #elif self.ID == CardName.REWIND:
        #elif self.ID == CardName.DARK_ENERGY:
        #elif self.ID == CardName.FUTURE_SHIFT:
        #elif self.ID == CardName.SINGULARITY:
        #elif self.ID == CardName.ANTIMATTER:

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
        if len(g.deck) != 0 and len(self.hand) < HAND_LIMIT:
            self.hand.append(g.deck.pop(0))

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


class Game():
    def __init__(self, player_one_name, player_two_name):
        self.player = []
        self.player.append(Player(player_one_name))
        self.player.append(Player(player_two_name))
        self.deck = []
        #INITIALIZE THE DECK FROM CSV FILE 
        with open('cards.csv', newline='') as csvfile: 
            text = csv.reader(csvfile, delimiter=';', quotechar='"') 
            #DECK LENGTH LEFT AT 10 CARDS FOR EASIER TESTING, MULTIPLY BY 4 WHEN COMPLETE 
            for row in text:
                c = Card(row[0], row[1], row[2], row[3]) 
                self.deck.append(c) 

        #SHUFFLE THE DECK 
        shuffle(self.deck) 

        self.discardPile = []

    #INSTALL CARD
    def install(self, cardIndex, playerIndex):
        player = self.player[playerIndex]

        assert(0 <= cardIndex < len(player.hand))
        card = player.hand.pop(cardIndex)
        player.tab.append(card) 
        card.onInstall()

    #DISCARD CARD
    def discard(self, cardIndex, playerIndex):
        player = self.player[playerIndex]

        assert(0 <= cardIndex < len(player.hand))
        card = player.hand.pop(cardIndex)
        self.discardPile.append(card)
        card.onDiscard()

    #DIFFUSE
    def diffuse(self, playerIndex, theirCardIndex, myCardIndex):
        player = self.player[playerIndex]
        otherplayer = self.player[1-playerIndex]

        defusedCard = otherplayer.tab[theirCardIndex]
        otherplayer.tab.pop(theirCardIndex)
        player.hand.pop(myCardIndex)
        defusedCard.onDiscard()




g = Game("PLAYER 1", "PLAYER 2")


    


#==========================================FUNCTIONS=========================================#

#PRINT LIST OF CARDS
def prettyPrintCards(cards):
    for i, card in enumerate(cards):
        print("card", i, ":", card)


#PRINT BOARD
def printBoard():
    g.player[0].printTab()
    g.player[1].printTab()

#GET PLAYER CHOICE OF CARD (TO INSTALL OR DISCARD)
def getChoice(choices, text):
    while True:
        print("Which card would you like to " + text + "?")
        prettyPrintCards(choices)
        choice = input()
        choice = int(choice)
        if 0 <= choice < len(choices):
            return choice

#PLAYER TURNS 
def playturn(playerIndex): 
    player = g.player[playerIndex]
    otherplayer = g.player[1-playerIndex]

    print(player.name + "'s turn: ")
    player.printHand()
    
    print("=================") 
    move = input("Choose from the following: 1. Draw, 2. Install, 3. Discard, 4. Diffuse\n")
    #DRAW 
    if move == "1": 
        player.draw()
    #INSTALL
    if move == "2": 
        # TODO: Implement this correctly
        cardIndex = getChoice(player.hand, "install")
        g.install(cardIndex, playerIndex) 
    #DISCARD 
    if move == "3": 
        cardIndex = getChoice(player.hand, "discard")
        g.discard(cardIndex, playerIndex)
    #DIffUSE 
    if move == "4": 
        theirCard = getChoice(otherplayer.tab, "diffuse")
        myCard = getChoice(player.hand, "use to diffuse " + otherplayer.tab[theirCard].name)
        g.diffuse(playerIndex, theirCard, myCard)
  
# =========================================MAIN GAME LOOP======================================== #
for i in range(STARTING_HAND_SIZE):
    g.player[0].draw()
    g.player[1].draw()

turnCounter = 0
while True: 
    print("#########################################") 
    print("Turn ", turnCounter)
    print("#########################################") 
    printBoard()
    playturn(turnCounter % 2)

    turnCounter += 1 

#=========================================DESIGN NOTES==========================================#
# 1. DECK[0] IS TOP OF DECK  i.e. deck.append() puts an item at the bottom of the deck
# REMEMBER TO SORT HAND EVERY TIME HAND IS TOUCHED:: CARDS THIS MIGHT APPLY TO:: ANTIMATTER; EXOTIC MATTER; RIFT; DEFLECTOR ###############TABS TOO 

#=========================================WHAT NOW?==========================================#
# assuming every card has no ability, get board working 
# score counting function in loop 
# instlal, diffuse, discard
# LEFT OFF LINE 15 TYRING TO LEFT JUSTIFY FIRST ELEMTN OF STIRNG 
# EVENT DRIVEN PROGRAMMING: define methods for Card class like onInstall() and onDiscard() that call other functions if the card has abilities activated. 
#=======================================TODO
#TODO IMPLEMENT "BACK": ALLOW USER TO CANCEL HIS CHOICE IF HE DIDNT MEAN TO CLICK INSTALL, DISCARD, WHATEVER  
#TODO "TRY CATCHING" AND HOW TO HANDLE BAD INPUT FROM USER  -> used in getChoice and playturn()
#TODO Defuse should not allow you to try to use something of low value to defuse something of higher value.
#TODO Add checks to Diffuse: currently does not validation on the cards selected, or even checks that there are cards to diffuse

#3. DISCARD
#4. INSTALL 
