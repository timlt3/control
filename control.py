from enum import Enum
import csv #for reading csv file 
from random import shuffle #for shuffling the deck
import operator  #FOR SORTING HANDS, lets you sort on class members

class Card(): 
    def __init__(self, name, value, color, description):
        self.name = name.strip()
        self.value = int(value)
        self.color = color.strip()
        self.description = description.strip()
#        self.onInstall = function()
#        self.onDiscards = function()

        #access enum with spaces replaced with _ 
        n =  self.name.replace(" ", "_") 
        self.ID = CardName[n]
    
    def __repr__(self): 
        return "Card()" 

    #allows print() to correctly handle Card class 
    def __str__(self): 
        seq ="%13s %2d %s %s" % (str(self.name) ,self.value , str(self.color) , str(self.description))
        return seq

#    def onInstall(self, card):
#        if self.ID == CardName.RIFT:
#        #RIFT DESTROYS A NOVA OR ALLOWS USER TO DRAW CARD
#        elif self.ID == CardName.EXOTIC_MATTER:
#        #CHAIN CELLS WITH 6 OR LESS CHARGE
#
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
    def __init__(self):
        self.hand = [] 
        self.tab = []
        self.name = str()

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

    

#INITIALIZE THE DECK FROM CSV FILE 
deck = []
with open('cards.csv', newline='') as csvfile: 
    text = csv.reader(csvfile, delimiter=';', quotechar='"') 
#DECK LENGTH LEFT AT 10 CARDS FOR EASIER TESTING, MULTIPLY BY 4 WHEN COMPLETE 
    for row in text:
        c = Card(row[0], row[1], row[2], row[3]) 
        deck.append(c) 

#SHUFFLE THE DECK 
shuffle(deck) 

#==========================================GLOBAL DATA=========================================#
#DISCARD PILE
discardPile = []

player1 = Player()
player1.name = "PLAYER 1"
player2 = Player() 
player2.name = "PLAYER 2" 

#==========================================FUNCTIONS=========================================#
#SORT HANDS 
#works by sorting list by card value i.e. WORKS FOR TABLEAUS
def sortHand(hand): 
    return sorted(hand, key=operator.attrgetter('value'))

#DEAL HAND 
def deal(): 
    for i in range(5): 
        draw(player1)
        draw(player2)

#PRINT HAND 
def printHand(hand): 
    h = sortHand(hand)
    p = 0
    for i in range(len(h)): 
        print("card", p,":", h[i]) 
        p += 1

#PRINT TAB 
def printTab(player): 
    print(player.name +"'s score is: ", getScore(player.tab))
    print(player.name +"'s Tableau is: ") 
    t1 = sortHand(player.tab) 
    for x in t1: 
        print(x)


def printBoard(player1, player2):
    printTab(player1)
    printTab(player2)

#GET SCORE
def getScore(tab): 
    #TODO sum elements of tableau
    score = 0
    for x in tab:
        score += x.value

    return score

#DRAW CARD
def draw(player): 
    if len(deck) != 0 and len(player.hand) < 7:
        player.hand.append(deck.pop(0))

#INSTALL CARD
def install(cardIndex, player):
    assert(0 <= cardIndex < len(player.hand))
    card = player.hand.pop(cardIndex)
    player.tab.append(card) 
    player.tab = sortHand(player.tab)

#DISCARD CARD
def discard(cardIndex, player):
    assert(0 <= cardIndex < len(player.hand))
    card = player.hand.pop(cardIndex)
    discardPile.append(card)
    card.onDiscard()

#GET PLAYER CHOICE OF CARD (TO INSTALL OR DISCARD)
def getChoice(player, text):
    while True:
        print("Which card would you like to " + text + "?")
        printHand(player.hand)
        choice = input()
        choice = int(choice)
        if 0 <= choice < len(player.hand):
            return choice

#PLAYER TURNS 
def playturn(player): 
    player.hand = sortHand(player.hand)
    print(player.name + "'s turn: ")
    printHand(player.hand)
    


    print("=================") 
    move = input("Choose from the following: 1. Draw, 2. Install, 3. Discard, 4. Diffuse\n")
    #DRAW 
    if move == "1": 
        draw(player)
    #INSTALL
    if move == "2": 
        # TODO: Implement this correctly
        cardIndex = getChoice(player, "install")
        install(cardIndex, player) 

    #DISCARD 
    if move == "3": 
        cardIndex = getChoice(player, "discard")
        discard(cardIndex, player)
    #DIffuse 
#    if move == str(4): 
  
#=========================================MAIN GAME LOOP========================================#
deal()
turnCounter = 0
while True: 
    printBoard(player1, player2)
    if turnCounter % 2 == 0:  
        playturn(player1)
    else: 
        playturn(player2)

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

#3. DISCARD
#4. INSTALL 
