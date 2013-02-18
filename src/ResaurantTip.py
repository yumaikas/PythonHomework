#Created for Professor Jennifer Cohen
#by Andrew Owen (aka yumaikas)
#From Chapter 2 problem 8

#Summary:
#This is a program that displays the amount of tip and
#tax for a restaurant meal.


#Give the percentages good names, since they could be used multiple times
#in later versions of this program
taxFactor = 0.07
tipFactor = 0.15

#Get the cost of the meal in a usable datatype
inCost = input("What was the cost of your meal? ")
cost = float(inCost)

tip = (cost * tipFactor)
tax = (cost * taxFactor)

#Use self-documenting format strings to display the tip and tax for the meal
print "You should pay a tip of: ${tip}.".format(tip=tip)
print "${tax} is the tax added to the meal.".format(tax=tax)
print "You pay a total of ${total}.".format(total=(tip + tax + cost))
