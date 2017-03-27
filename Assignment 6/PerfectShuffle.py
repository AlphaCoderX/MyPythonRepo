#Programmer Raphael Heinen
#Date 3/26/17
#Version 1.0
import functions
import random
rank = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
suit = ['Clubs','Hearts','Diamonds','Spades']

#builds a deck from rank and suit adding 'of' 
def buildDeck(rank,suit):
    num = -1
    num2 = 0
    deck = []
     
    while num2 != 13:
        num = -1
        for i in suit:
            num +=1
            deck.append(("%s of %s" % (rank[num2],suit[num])))
            if num == 3:
                num2 +=1
            
    return deck
#shuffles and interleaves cards   
def shuffle(deck):
   shuffled = []
   half = deck[:26] 
   half2 = deck[26:]
   i = 0
  
   while i < 26:
       shuffled.append(half[i])
       shuffled.append(half2[i])
       i+=1
       
   return shuffled
#delas top 5 cards in deck
def deal(deck):
    top5 = deck[:5]
    
    return top5
    
def main():
   myDeck = buildDeck(rank,suit)
   times = functions.userInt("How many times do you want me to shuffle?:")

   for i in range(times):
      myDeck = shuffle(myDeck)
   print deal(myDeck)
    
main()
    
    
