import fileReader
import random

maxWeight = 500

def initialTemp():
    #no idea how to initialize this
    T = 40000
    return T

def initialSolution(listOfItems):
    numOfItems = 20
    initialScore = 0
    for i in range(0, 20):
        listOfItems[random.randint(0, 200)][2] = 1

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

def driver():
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)
    initialUtility = calcUtility(listOfItems)
    initialWeight = calcWeight(listOfItems)

driver()
