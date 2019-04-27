from enum import Enum
import csv #for reading csv file 
from random import shuffle #for shuffling the deck
import operator  #FOR SORTING HANDS, lets you sort on class members

from CardName import CardName
from Card import Card
from Constants import *
from Player import Player
from Util import *
import Game

Game.createGame("PLAYER 1", "PLAYER 2")
g = Game.getGame()

#==========================================FUNCTIONS=========================================#

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
