#Programmer Raphael Heinen
#Date 4/2/17
#Version 1.0
import functions
import os

wordlist = []
wordlist2 = []
wordlist3 = []
wordlist4 = []

filelist = []

def readFile():

    for file in os.listdir("."):
        
        if file.endswith(".txt"):
            filelist.append(file)
            print(os.path.join(".", file))
    return filelist

def user(filelist,wordlist):

    a = open(filelist[0])
    for word in a:
        w = word.strip().upper()
        wordlist.append(w)
        
        b = open(filelist[1])
    for word in b:
        w = word.strip().upper()
        wordlist2.append(w)
        
        c = open(filelist[2])
    for word in c:
        w = word.strip().upper()
        wordlist3.append(w)
        
        d = open(filelist[3])
    for word in d:
        w = word.strip().upper()
        wordlist4.append(w)
        
    term = functions.userString("Enter a search term:").upper()
    count = 0
    
    for i in wordlist:
        if term in i:
            count += 1
            
            print "%s: %s" % (filelist[0], i)
            
    for i in wordlist2:
        if term in i:
            count += 1
            
            print "%s: %s" % (filelist[1], i)

    for i in wordlist3:
        if term in i:
            count += 1
            
            print "%s: %s" % (filelist[2], i)

    for i in wordlist4:
        if term in i:
            count += 1
            
            print "%s: %s" % (filelist[3], i)

    print "I found %s results" %count
def main():
    readFile()
    user(filelist,wordlist)

main()
