#Programmer Raphael Heinen
#Date 2/19/17
#Version 2.0

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
# Runs the program in a loop and  asks the user 
# to enter a bird name or exit and then looks up 
# the sighting count for that bird in the specified 
# dictionary (d).
# ------------------------------------------------------------
def askUser(d):
    checker = True
    seen = []
    name = []
    num = 0
    num2 = "None"
    check = 0
    while checker:
        names = functions.userString("Enter a bird name and 'exit' to stop:").lower()
        
        if names in d:
            sighting = d[names]
            seen.append(sighting)
            name.append(names.title())
            
#looks for the bird seen the most often

            if sighting >= max(seen):
                num = seen.index(max(seen))
                num2 = name[num]
                check = check + 1

        elif names not in d:
            sighting = 0
            
            if names == 'exit':
                checker = False
                
            
        print "I've seen that bird %s time(s)" %sighting
        print "Bird seen the most: %s \n" %num2
        
       
def main():
    data = countBirds('Birds.txt')
    askUser(data)
    
main()
