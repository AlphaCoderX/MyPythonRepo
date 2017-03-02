#Programmer Raphael Heinen
#Date 2/26/17
#Version 1.0

def readData(filename):
    cubeHead = []
    sqMaster = []
    advTwist = []
    inteTurn = []
    avgMover = []
    pathetic = []
#adds all of the data to a list
#and adds data in that a range to
#the appropriate list(s)
    for line in open(filename):
        temp = line.split(",")
        player = temp[0].strip()
        time = float(temp[1])
        
        if int(time) in range(0,9):
            cubeHead.append(player)
            
        if int(time) in range(10,20):
            sqMaster.append(player)
            
        if int(time) in range(20,30):
            advTwist.append(player)

        if int(time) in range(30,40):
            inteTurn.append(player)
            
        if int(time) in range(40,60):
            avgMover.append(player)
            
        if int(time) in range(60,9999999):
            pathetic.append(player)
            
    return cubeHead,sqMaster,advTwist,inteTurn,avgMover,pathetic

#prints the results from the lists           
def results(player):
    print "Cube Head(0-9.99):"
    for n in player[0]: print "      %s" %n
    print ""
    print "Square Master(10-19.99):"
    for n in player[1]: print "      %s" %n
    print ""
    print "Advanced Twister(20-20.99):"
    for n in player[2]: print "      %s" %n
    print ""
    print "Intermediate Turner(30-39.99):"
    for n in player[3]: print "      %s" %n
    print ""
    print "Average Mover(40-59.99):"
    for n in player[4]: print "      %s" %n
    print ""
    print "Pathetic(60 and beyond):"
    for n in player[5]: print "      %s" %n
            
def main():
    a = readData("timings.txt")
    results(a)
main()
