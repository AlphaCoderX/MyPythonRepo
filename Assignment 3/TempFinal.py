#Programmer Raphael Heinen
#Date 2/2/17
#Version 2.0
import functions
data = []
file = open('temp.txt','r')

#opens and adds the text file to a list
def readTemps():
    for temp in file.read().split():
        data.append(float(temp))
    return data
    
#calculates and returns average
def calcAvg(temp,start,stop):
    total = 0
    for x in range(start,stop):
        total = (total + data[x])
        num = stop - start
        average = total/num

    return average
#finds and returns the positive numbers   
def count(temp, start, stop):    
    counter = 0
    for x in range(start,stop):
        if data[x] > 0:
           counter += 1
        
    return counter       
#gets user input for the percentage split
#and returns the appropriate number
def user():
        
    percent = functions.userInt("Enter the percentage split: %")
    num = float(percent) / 100 * 116 
    number = int(num)
           
    return number
        
def main():
    
     finalnum = user()
     finalnum2 = 116 - finalnum
     temps = readTemps()
     counter1 = count(temps,0,finalnum)
     counter2 = count(temps,finalnum,116)
     deviation1 = calcAvg(temps,0,finalnum)
     deviation2 = calcAvg(temps,finalnum,116)  
     print "During the first %s years, the average deviation from the temprature anomoly was %s" % (finalnum, deviation1)
     print "During the first %s years, %s had a positive temprature anomoly" % (finalnum , counter1)
     print "During the last %s years, the average deviation from the temprature anomoly was %s" % (finalnum2, deviation2)
     print "During the last %s years, %s had a positive temprature anomoly" % (finalnum2, counter2)

main()
