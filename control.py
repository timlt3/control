import csv #for reading csv file 
from random import shuffle #for shuffling the deck
import operator  #FOR SORTING HANDS, lets you sort on class members

class Card: 
    def __init__(self, name, value, color, description):
        self.name = name.strip()
        self.value = int(value)
        self.color = color.strip()
        self.description = description.strip()
    
    def __repr__(self): 
        return "Card()" 
    def __str__(self): 
        seq ="%13s %2d %s %s" % (str(self.name) ,self.value , str(self.color) , str(self.description))
        return seq



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

#PLAYER HANDS 
hand1 = [] 
hand2 = [] 

#SORT HANDS
def sortHand(hand): 
    return sorted(hand, key=operator.attrgetter('value'))

def draw(playerHand): 
    if len(deck) != 0 and len(playerHand) < 7:
        playerHand.append(deck.pop(0))

def deal(): 
    for i in range(5): 
        draw(hand1) 
        draw(hand2) 

#PRINT HAND 
def printHand(hand): 
    h= sortHand(hand)
    for i in range(len(h)): 
        print(h[i]) 


#PLAYER TURNS 
def playturn(hand): 
    printHand(hand)
    print("=================") 
    move = input("Choose from the following: 1. Draw, 2. Install, 3. Discard, 4. Diffuse\n")
    #DRAW 
    if move == "1": 
        draw(hand)
    #INSTALL
#    if input == str(2): 
    #DISCARD 
#    if input == str(3): 
    #DIffuse 
#    if input == str(4): 

# "MAIN" FUNCTION 
deal()
while True: 
    playturn(hand1)

################DESIGN NOTES ############## 
# 1. DECK[0] IS TOP OF DECK  i.e. deck.append() puts an item at the bottom of the deck
# LEFT OFF LINE 15 TYRING TO LEFT JUSTIFY FIRST ELEMTN OF STIRNG 
