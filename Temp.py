#Programmer Raphael Heinen
#Date 2/2/17
#Version 1.0
data = []
file = open('temp.txt','r')
#reads and adds the text file to a list
def readTemps():
    for temp in file.read().split():
        data.append(float(temp))
    return data
#calculates and returns average    
def calcAvg(temp,start,stop):
    total = 0
    for x in range(start,stop):  
        total = (total + data[x])
        num = x + 1

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
    
def main():
     temps = readTemps()
     counter1 = count(temps,0,81)
     counter2 = count(temps,81,116)
     deviation1 = calcAvg(temps,0,81)
     deviation2 = calcAvg(temps,81,116)
     print "During the first 81 years, the average deviation from the temprature anomoly was %s" % deviation1
     print "During the first 81 years, %s had a positive temprature anomoly" % counter1
     print "During the last 35 years, the average deviation from the temprature anomoly was %s" % deviation2
     print "During the last 35 years, %s had a positive temprature anomoly" % counter2

main()

