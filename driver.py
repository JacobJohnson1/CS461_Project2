from pickle import FALSE, TRUE
from numpy import diff
import fileReader
import random
import copy
import math
from numpy import exp
import calculations

def initialSolution(listOfItems):
    numOfItems = 20
    for i in range(0, numOfItems):
        listOfItems[random.randint(0, len(listOfItems)-1)][2] = 1

def proposedChange(listOfItems):
    copyList = copy.deepcopy(listOfItems)
    changedItemIndex = random.randint(0, len(listOfItems)-1)
    if copyList[changedItemIndex][2] == 0:
        copyList[changedItemIndex][2] = 1
    elif copyList[changedItemIndex][2] == 1:
        copyList[changedItemIndex][2] = 0
    return(copyList)

def checkChange(initialList, copyList, temp):
    initialUtility = calculations.calcUtility(initialList)
    copyUtility = calculations.calcUtility(copyList)
    difference = (initialUtility - copyUtility)
    probability = math.exp((-difference) / temp)
    if (difference < 0) or (random.random() > probability):
        initialList = copy.deepcopy(copyList)
        return True
    else: return False

def tempAndCounters(attmeptCounter, changeCounter, temp, iterationCounter):
    if (changeCounter == 4000) or (attmeptCounter == 40000):
        temp *= 0.9
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
    print('Total Utility: %s' % calculations.calcUtility(listOfItems))
    print('Total Weight: %s' % calculations.calcWeight(listOfItems))

def main():
    temp = 400
    changeCounter = 0
    consecutiveAttemptCounter = 0
    iterationCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)

    while True:
        copyList = proposedChange(listOfItems)
        changeBool = checkChange(listOfItems, copyList, temp)
        if changeBool:
            changeCounter += 1
        consecutiveAttemptCounter += 1
        if (consecutiveAttemptCounter == 40000) and (changeCounter == 0):
            printFunction(listOfItems)
            break
        tempAndCounters(consecutiveAttemptCounter, changeCounter, temp, iterationCounter)

if __name__ == "__main__":
  main()