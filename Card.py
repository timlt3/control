from CardName import CardName
from Constants import *

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
