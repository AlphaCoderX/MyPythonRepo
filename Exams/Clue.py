#Programmer Raphael Heinen
#Date 4/30/17
#Version 1.0
import functions

suspects = ["Miss Scarlet", "Col Mustard", "Mr Green"]
weapons = ["Candlestick","Wrench","Pipe"]

#Appends the suspects and weapons to one list
def clue():
    a = []
    for s in suspects:
        for w in weapons:
            a.append("%s with a %s" % (s,w))

    return a

#asks the user questions about the
#suspects and weapons used and searches
#and removes the items entered from the list
def ask(a):
    print "%s possibilities left." % len(a)
    ask = functions.userString("Is this a clue about a weapon or a suspect? (w or s)?")
    
    if ask == "w":
        wep = functions.userString("Enter the weapon that was not used %s :" % weapons).title()
        if any(wep in s for s in a):
            m = [s for s in a if wep in s]
            for z in m:
                a.remove(z)
        else:
            print "Nothing found for '%s', Try again." % wep
            
    if ask == "s":
        sus = functions.userString("Enter the innocent suspect %s :" % suspects).title()
        if any(sus in s for s in a):
            m = [s for s in a if sus in s]
            for z in m:
                a.remove(z)
                
        else:
            print "Nothing found for '%s', Try again." % wep
    
#runs the program and prints
#the final suspect
def main():
    a = clue()
    while len(a) != 1:
        ask(a)
        
    for x in a:
        print "\n It was %s" %x

main()
