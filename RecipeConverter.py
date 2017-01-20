#Programmer Raphael Heinen
#Date 1/19/17
#Version 1.0
print "-- Original Recipe --"
print "Enter the amount of flour (cups): ",
flour = raw_input()
print "Enter the amount of water (cups): ",
water = raw_input()
print "Enter the amount of salt (teaspoons): ",
salt = raw_input()
print "Enter the amount of yeast (teaspoons): ",
yeast = raw_input()
print "Enter the loaf adjustment factor (e.g. 2.0 double the size): ",
factor = raw_input()

#adjusts recipe based on user input factor
flour = float(flour) * float(factor)
water = float(water) * float(factor)
salt =  float(salt) * float(factor)
yeast = float(yeast) * float(factor)

print " "
print "-- Modified Recipe --"
print "Bread Flour: %s cups." % flour
print "Water: %s cups." % water
print "Salt: %s teaspoons." % salt
print "Yeast: %s teaspoons." % yeast
print "Happy Baking!",
print " "

#converts current cup(s) measurement(s) to grams
flour2 = flour * 120
water2 = water * 237
salt2 = salt * 5
yeast2 = yeast * 3


print "-- Modified Recipe in Grams --"
print "Bread Flour: %s g." % flour2
print "Water: %s g." % water2
print "Salt: %s g." % salt2
print "Yeast: %s g." % yeast2
print "Happy Baking!",


