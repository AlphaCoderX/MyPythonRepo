#Programmer Raphael Heinen
#Date 2/12/17
#Version 1.0

#reads the data from a specified text file and
#returns the data as a list
def readData(filename):
    speeds = []
    file = open(filename)
    
    for data in file:
        speeds.append(int(data))
        
    return speeds

#averges the speeds from the specified text file
#and returns the average
def getAverage(l):
    total = 0
    for x in l:
        total = float(total + x)    
        average = total / len(l)
        
    return average
    
#counts the numbers of speeds that exceeded
#maxSpeed and returns the counted numbers.
def countSpeeders(l, maxSpeed):
    count = 0
    for x in l:
        if x > maxSpeed:
            count += 1
            
    return count        
    
#finds the number of people speeding during
#and not during rush hour, as well as the average speed(s).
#it also determines the fine amount based on when the
#driver was speeding.
def main():
    
    rush = readData("data-rush.txt")
    norush = readData("data-not-rush.txt")
    avgrush = getAverage(rush)
    avgnorush = getAverage(norush)
    
    rushHour = countSpeeders(rush, 69)
    notRushHour = countSpeeders(norush, 69)
    
    rushFine = 150 * rushHour
    norushFine = 100 * notRushHour

    print "The average speed during rush hour was %.2f" % avgrush
    print "The average speed not during rush hour was %.2f" % avgnorush
    print "There were %s speeders during rush hour.  Total fine = $%s" % (rushHour, rushFine)
    print "There were %s speeders not during rush hour.  Total fine = $%s" % (notRushHour, norushFine)

main()
