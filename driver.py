from pickle import FALSE, TRUE
from numpy import diff
import fileReader
import random
import copy
import math
from numpy import exp

maxWeight = 500

def initialSolution(listOfItems):
    numOfItems = 20
    for i in range(0, numOfItems):
        listOfItems[random.randint(0, len(listOfItems)-1)][2] = 1

def calcUtility(listOfItems):
    totalUtility = 0.0
    for i in range(0, len(listOfItems)):
        if listOfItems[i][2] == 1:
            totalUtility += listOfItems[i][0]
    weight = calcWeight(listOfItems)
    totalUtility = overWeightCheck(totalUtility, weight)
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

def proposedChange(listOfItems):
    copyList = copy.deepcopy(listOfItems)
    changedItemIndex = random.randint(0, len(listOfItems)-1)
    if copyList[changedItemIndex][2] == 0:
        copyList[changedItemIndex][2] = 1
    elif copyList[changedItemIndex][2] == 1:
        copyList[changedItemIndex][2] = 0
    return(copyList)

def checkChange(initialList, copyList, temp):
    initialUtility = calcUtility(initialList)
    copyUtility = calcUtility(copyList)
    # TEST
    # print('initial utility: %s' % initialUtility)
    # print('copy utility: %s' % copyUtility)
    difference = (initialUtility - copyUtility)
    probability = math.exp((-difference) / temp)
    if (difference < 0) or (random.random() > probability):
        initialList = copy.deepcopy(copyList)
        # print('change occurred')
        return True
    else: return False

def tempReduction(attmeptCounter, changeCounter, temp, iterationCounter):
    if (changeCounter == 4000) or (attmeptCounter == 40000):
        temp = (temp * 0.9)
        iterationCounter += 1
        print('Attempts: %s\tChanges: %s\t Temperature: %s\tIterations: %s' % (attmeptCounter, changeCounter, temp, iterationCounter))
        changeCounter = 0
        attmeptCounter = 0

def printFunction(listOfItems):
    print('Final list of items packed in car:')
    print('Utility \t Weight')
    for i in range(0, len(listOfItems)-1):
        if listOfItems[i][2] == 1:
            print('%s \t\t %s' % (listOfItems[i][0], listOfItems[i][1]))
    print('Total Utility: %s' % calcUtility(listOfItems))
    print('Total Weight: %s' % calcWeight(listOfItems))

def main():
    temp = 400
    changeCounter = 0
    consecutiveAttemptCounter = 0
    iterationCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)
    # printFunction(listOfItems)

    while True:
        copyList = proposedChange(listOfItems)
        # printFunction(listOfItems)
        # printFunction(copyList)
        changeBool = checkChange(listOfItems, copyList, temp)
        if(changeBool == True):
            changeCounter += 1
        consecutiveAttemptCounter += 1
        tempReduction(consecutiveAttemptCounter, changeCounter, temp, iterationCounter)
        if (consecutiveAttemptCounter == 40000) and (changeCounter == 0):
            printFunction(listOfItems)
            break

if __name__ == "__main__":
  main()