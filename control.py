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
#PLAYER HANDS 
hand1 = [] 
hand2 = [] 

#PLAYER TABLEAU
tab1 = []
tab2 = []

#DISCARD PILE
discardPile = []

#==========================================FUNCTIONS=========================================#
#SORT HANDS 
#works by sorting list by card value i.e. WORKS FOR TABLEAUS
def sortHand(hand): 
    return sorted(hand, key=operator.attrgetter('value'))

#DEAL HAND 
def deal(): 
    for i in range(5): 
        draw(hand1) 
        draw(hand2) 

#PRINT HAND 
def printHand(hand): 
    h = sortHand(hand)
    p = 0
    for i in range(len(h)): 
        print("card", p,":", h[i]) 
        p += 1

#PRINT BOARD 
def printBoard(tab1, tab2): 
    print("Player 1's score is: ", getScore(tab1))
    print("Player 1's Tableau is\n") 
    t1 = sortHand(tab1) 
    for x in t1: 
        print(x)

    t2 = sortHand(tab2)
    for x in t2:
        print(x)

#GET SCORE
def getScore(tab): 
    #TODO sum elements of tableau
    score = 0
    for x in tab:
        score += x.value

    return score

#DRAW CARD
def draw(playerHand): 
    if len(deck) != 0 and len(playerHand) < 7:
        playerHand.append(deck.pop(0))

#INSTALL CARD
def install(card, tab):
    tab.append(card)

#DISCARD CARD
def discard(cardIndex, hand):
    assert(0 <= cardIndex <= len(hand))
    card = hand.pop(cardIndex)
    discardPile.append(card)
    card.onDiscard()

#GET PLAYER CHOICE OF CARD (TO INSTALL OR DISCARD)
def getChoice(hand, text):
    while True:
        print("Which card would you like to" + text + "?")
        printHand(hand)
        choice = input()
        if 0 <= int(choice) <= len(hand):
            return choice

#PLAYER TURNS 
def playturn(hand): 
    printHand(hand)
    print("=================") 
    move = input("Choose from the following: 1. Draw, 2. Install, 3. Discard, 4. Diffuse\n")
    #DRAW 
    if move == "1": 
        draw(hand)
    #INSTALL
    if move == "2": 
        # TODO: Implement this correctly
        install(hand)

    #DISCARD 
    if move == "3": 
        cardIndex = getChoice()
        discard(cardIndex, hand)
    #DIffuse 
#    if move == str(4): 
  
#=========================================MAIN GAME LOOP========================================#
deal()
turnCounter = 0
while True: 
    if turnCounter % 2 == 0:  
        playturn(hand1)
    else: 
        playturn(hand2)

    turnCounter += 1 

#=========================================DESIGN NOTES==========================================#
# 1. DECK[0] IS TOP OF DECK  i.e. deck.append() puts an item at the bottom of the deck

#=========================================WHAT NOW?==========================================#
# assuming every card has no ability, get board working 
# score counting function in loop 
# instlal, diffuse, discard
# LEFT OFF LINE 15 TYRING TO LEFT JUSTIFY FIRST ELEMTN OF STIRNG 
# EVENT DRIVEN PROGRAMMING: define methods for Card class like onInstall() and onDiscard() that call other functions if the card has abilities activated. 
#=======================================TODO
#TODO IMPLEMENT "BACK": ALLOW USER TO CANCEL HIS CHOICE IF HE DIDNT MEAN TO CLICK INSTALL, DISCARD, WHATEVER  
#TODO "TRY CATCHING" AND HOW TO HANDLE BAD INPUT FROM USER  -> used in getChoice and playturn()
