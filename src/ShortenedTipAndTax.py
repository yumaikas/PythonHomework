#For amusment, a two line version of the tip & tax program
cost = float(input("What was the cost fo your meal? "))
print "You should pay a tip of: ${tip}. \n${tax} is the tax added to the meal.".format(tip = cost * 0.15, tax = cost * 0.07)
