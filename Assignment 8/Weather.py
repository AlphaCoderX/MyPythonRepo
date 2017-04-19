#Programmer Raphael Heinen
#Date 4/18/17
#Version 1.0
import json
import urllib2
import functions

    
def readJson():
    
    city = functions.userString("Please enter a zip code or city name:")
    print " "
    url = 'https://api.apixu.com/v1/current.json?key=dcb629e49c894492b66150648172303&q=' + city
    jsonTxt = urllib2.urlopen(url).read()
    apixu = json.loads(jsonTxt)
    
    return apixu


def printer(apixu):
    
    
        print "Here is the weather for %s, %s" % (apixu['location']['name'],apixu['location']['region'])
        print "%s and %s degrees (F)." % (apixu['current']['condition']['text'],apixu['current']['temp_f'])
        print "It actually feels like %s (F)." % apixu['current']['feelslike_f']
        print " "
        again = functions.userString("Want to check another location? (y/n):")
 
        
        return again
            
    

def main():
    ask = True
    while ask == True:  
        r = readJson()
        a = printer(r)
        
        if a == 'n':
            ask = False
            
        if a == 'y':
            ask = True

main()