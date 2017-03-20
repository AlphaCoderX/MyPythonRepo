#Programmer Raphael Heinen
#Date 3/19/17
#Version 1.0

import random
import functions

choices = ['bird','dog','snake','fish','cat','mouse','starfish','woodchuck','crab']
cards = [0,1,2,3,4,5,6,7,8,0]

#shuffles the card data
def shuffle():
    random.shuffle(choices)
    random.shuffle(cards)
    
    return (choices, cards)
    
    
#asks user for their choices and keeps
#going till there is a match
def askUser(data):
    nopairs = True
    count = 1
    dontprint = False
    
    while nopairs:
        dontprint = False
        ask = functions.userInt("Pick the first card to turn over (0-9):")
        ask2 = functions.userInt("Pick the second card to turn over (0-9):")
        if ask == ask2 or ask < 0 or ask2 < 0 or ask > 9 or ask2 > 9:
            print "You must pick a different card and the card must be from 0-9."
            dontprint = True
        
        elif choices[cards[ask]] == choices[cards[ask2]]:
            print "You win! It took you %s tries." %count
            nopairs = False
            
        if dontprint == False:
            print "Card %s is a %s" %(ask,choices[cards[ask]])
            print "Card %s is a %s" %(ask2,choices[cards[ask2]])
            count += 1

def main():
    askUser(shuffle())
main()