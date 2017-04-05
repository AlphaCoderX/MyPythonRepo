import json
import functions
#reads the JSON file and adds it
#to a dictionary and returns it
def read():
    jsonTxt = ""
    f = open('classes.json')
    for line in f:
        line = line.strip()
        jsonTxt = jsonTxt + line
    classes = json.loads(jsonTxt)
    
    return classes

#Asks the user for input and returns
#the dictionary items based on the input
def askUser(classes):    
    print "**Class Search**"
    name = functions.userString("Enter a Professor:")
    for cls in classes:
        if cls["Professor"] == name:
            for c in cls["Class"]:
                print "Class: %s"  % c
            print "Time: %s" % cls["Time"]
            print "Location: %s \n" % cls["Location"]

def main():
    askUser(read())
        
main()
    