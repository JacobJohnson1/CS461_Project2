import fileReader
import random
import copy

maxWeight = 500

def initialTemp():
    #no idea how to initialize this
    T = 40000
    return T

def initialSolution(listOfItems):
    numOfItems = 20
    initialScore = 0
    for i in range(0, 20):
        listOfItems[random.randint(0, 400)][2] = 1

def calcUtility(listOfItems):
    totalUtility = 0.0
    for i in range(0, len(listOfItems)):
        if listOfItems[i][2] == 1:
            totalUtility += listOfItems[i][0]
    return(totalUtility)

def calcWeight(listOfItems):
    totalWeight = 0.0
    for i in range(0, len(listOfItems)):
        if listOfItems[i][2] == 1:
            totalWeight += listOfItems[i][1]
    return(totalWeight)
    
def overWeightCheck(utility, weight):
    if weight > maxWeight:
        penalty = ((weight - maxWeight) * 20)
        utility -= penalty
    return utility

def makeChange(listOfItems):
    copyList = copy.deepcopy(listOfItems)
    changedItem = random.randint(0,400)
    if copyList[changedItem][2] == 0:
        copyList[changedItem][2] = 1
    elif copyList[changedItem][2] == 1:
        copyList[changedItem][2] = 0
    # CHECK IF THIS CHANGE IMPROVES THE UTILITY/WHETHER TO MAKE THIS CHANGE
    # IF YES, listOfItems = copyList

# RESEARCH BEST WAY TO REDUCE TEMP 
# ALSO, WHAT TO DO WHEN TEMP IS == 0?
def tempReduction(attmeptCounter, changeCounter, temp):
    if changeCounter == 4000:
        temp = (temp * 0.99)
    elif attmeptCounter == 40000:
        temp = (temp * 0.99)

def stopTime():
    if (attemptCounter == 40000) and (changeCounter == 0):
        #time to stop
        #maybe implement as a while loop in driver

def driver():
    changeCounter = 0
    attemptCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)
    initialUtility = calcUtility(listOfItems)
    initialWeight = calcWeight(listOfItems)

driver()
