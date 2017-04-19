#Programmer Raphael Heinen
#Date 4/18/17
#Version 1.0

#reads in the JSON file and returns a dictionary
import json
import functions

def read():
    jsonTxt = ""
    f = open('PetStore.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    petinfo = json.loads(jsonTxt)
    
    return petinfo
    
#asks the user to enter a category
#or keyword, loops through the dictionaries 
#and returns the items found
def askUser(petinfo):
    
    ask = functions.userString("Search by category (c) or keyword (k)?").lower()
    
    if ask == "c":
        ask2 = functions.userString("Enter a category:").title()
        
        for x in petinfo:
            if x['Category'] == ask2:
                print x['Product'] + " - $%s" % x['Price']
                
    if ask == "k":
        ask3 = functions.userString("Enter a keyword").title()
        
        for w in petinfo:
            if ask3 in w['Product']:
                print w['Product'] + " - $%s" % w['Price']
                
                
def main():
    
    info = read()
    askUser(info)
    
main()