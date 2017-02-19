#Programmer Raphael Heinen
#Date 2/19/17
#Version 1.0

# ------------------------------------------------------------
# For a badge do the following:
#
# After each user query print out the bird that has been seen 
# most often.  If there is a tie, print all of birds that are 
# tied for most sightings.
#
# Allow the user to enter a bird name as often as the like.
# When they want to stop entering bird names they can type 
# 'Exit'.
#
# Make the lookup case insensitive.  In other words, I should
# be able to type ROBIN or RoBiN and get the count for Robin.
# ------------------------------------------------------------

# ------------------------------------------------------------
# Reads the specified file (filename) and returns a dictionary 
# whose keys are bird names and whose values are the number of 
# times the bird has been seen.
# ------------------------------------------------------------
import functions

def countBirds(filename):
    birdData = {}
    
    for line in open(filename):
	line = line.split(', ')
	bird = line[0].lower()
	num = int(line[1])

	if bird not in birdData:
	    birdData[bird] = num
	    
	else:
	    birdData[bird] += num

      
    return birdData

# ------------------------------------------------------------
# Asks the user to enter a bird name and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    
        names = functions.userString("Enter a bird name or 'exit' to stop:").lower()
        
        if names in d:
            sighting = d[names]
        
        else:
            sighting = 0
            
        if names == 'exit':
            sighting = "0"
    
        return sighting
        
def main():
    checker = True

    while checker: 
        birdData = countBirds('Birds.txt')
        user = askUser(birdData)


        print "I've seen that bird %s time(s)" %user
        
        
        if user == "0":
            user = 0
            checker = False
            
        
    
main()
