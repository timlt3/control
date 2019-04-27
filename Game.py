from enum import Enum
import csv #for reading csv file 
from random import shuffle #for shuffling the deck
import operator  #FOR SORTING HANDS, lets you sort on class members

from CardName import CardName
from Card import Card
from Constants import *
import Player

class Game():
    def __init__(self, player_one_name, player_two_name):
        self.player = []
        self.player.append(Player.Player(player_one_name))
        self.player.append(Player.Player(player_two_name))
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

# FIXME: Terrible hack
def createGame(name1, name2):
    global g
    g = Game(name1, name2)

def getGame():
    global g
    return g
