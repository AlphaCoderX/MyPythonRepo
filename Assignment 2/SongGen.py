#Programmer Raphael Heinen
#Date 1/26/17
#Version 1.0
import functions

val = 1
songparts = []
chorus = []
verses = ["first", "second","third","fourth"]
#takes the user input for the verses, 
#makes it uppercase and censors 'cookies'
for verse in verses:
    song = functions.userString("Enter the %s verse: " % verse)
    song = song.replace('cookies','_______')
    songparts.append(song.upper())
 
#takes the input and factor for chorus and makes it lowercase.
chorus = functions.userString("Enter the chorus: ")     
factor = functions.userInt("Enter the chorus repeat:" )
chorus = (chorus.lower() + " ")

#adds the chorus strings to the rest of the song.
for lyrics in range(1,4):
    songparts.insert(val,chorus * factor)
    val += 2
#adds the extra chorus bit and plays it again.
songparts.insert(7,chorus * factor + chorus) 
songparts = songparts * 2
songparts.insert(8,"...One more time!...")

print songparts

for lyrics in songparts:
    print lyrics
