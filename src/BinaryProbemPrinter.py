#Created for Professor Jennifer Cohen
#By Andrew Owen (yumaikas)
#For COP-1000
#This program prints out the steps of parsing a binary number and
#adds commentary. This enables a student to cheat using this program.
#I HAVE NOT used it for this purpose.

#Specific imports
from collections import namedtuple
from string import join

#A couple of constant functions for comparisons below, since python doesn't have syntactic constansts
def ONE():
    return "1"
def ZERO():
    return "0"
#Create a namedtuple to hold the numbers in each step.
#We don't need a full blown class here since we are only
#storing data for a trival problem.
numbersForStep = namedtuple('numbersForStep', 'binVal, twoFactor, workingNumber')

number = int(raw_input("What number do you want to convert to binary? "))
print "The number in binary is {number:b}".format(number=number)
#Now we give the functions that will be used.

def MaxMultipleOfXUnder(x, num, multiple = 1):
    #Look for the first multiple of two that is higher than the number given
    if multiple * x > num:
    #And return the mutiple of x lower than than the first multiple
        return multiple
    #Otherwise repeat
    else:
        return MaxMultipleOfXUnder(x, num, (multiple * x))

def BuildBinaryStringAndCommentary(number):
    #This function builds the needed information for outputting the steps of
    #the problem in a human readable way
    twoFactor = MaxMultipleOfXUnder(2, number)
    stepNums = []
    commentary = []
    binPlaceVal = ""
    #For each power of two, create the appropriate commentary for it, based on whether
    #a 0 or 1 should be used.
    skipping = False
    while twoFactor >= 1:
        if number >= twoFactor:
            binPlaceVal = ONE()
            commentary.append("Subtracting {twoFactor} from {num}".format(twoFactor=twoFactor, num=number))
            number -= twoFactor
            skipping = False
        else:
            binPlaceVal = ZERO()
            if not skipping:
                commentary.append("Skipping {0}".format(twoFactor))
                skipping = True
            else:
                commentary.append("and " + str(twoFactor))
        stepNums.append(numbersForStep(binPlaceVal, twoFactor, number))
        twoFactor /= 2
    return [stepNums, commentary]

def OutputProblem(number):
    
    numberedSteps, commentary = BuildBinaryStringAndCommentary(number)
    #Find how long the longest string in the twoPowers list is
    maxLen = max([len(str(step.twoFactor)) for step in numberedSteps])

    #Format the numbers in a nicely tabbed manner
    def justifyItems(listNum):
        for item in listNum:
            yield str(item).rjust(maxLen + 1)
            
    #Justify each string from numberedSteps based on the longest
    #string length we found above 
    factorsOfTwo = justifyItems([step.twoFactor for step in numberedSteps])
    binaryValues = justifyItems([step.binVal for step in numberedSteps])
    #join the strings to form the table we will be using
    numberStrip = join(factorsOfTwo, '|')
    binaryStrip = join(binaryValues, '|')
    #print the setup information
    print "The work for the calculation is below:"
    print numberStrip
    print binaryStrip
    print ""
    #Print out the commentary lines where they matter
    for i in range(len(commentary)):
        comm = commentary[i]
        nums = numberedSteps[i]
        
        print "//{0}".format(comm)
        if nums.binVal == ONE():
            #Because the steps are recorded above after the changes
            #have been made to the workingNumber, we have to add
            #the workingNumber to the twoFactor to the result before the subtraction
            print str(nums.workingNumber + nums.twoFactor).rjust(maxLen + 1)
            print "-{0}".format(str(nums.twoFactor).rjust(maxLen))
            print "={0}".format(str(nums.workingNumber).rjust(maxLen))
            print ""
#Call the problem output function to drive the program
OutputProblem(number)
        




