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

def displayResults(listOfItems):
    print('Final list of items packed in car:')
    print('Utility \t Weight')
    for i in range(0, len(listOfItems)-1):
        if listOfItems[i][2] == 1:
            print('%d \t\t %d' % (listOfItems[i][0], listOfItems[i][1]))
    print('Total Utility: %d' % calculations.calcUtility(listOfItems))
    print('Total Weight: %d' % calculations.calcWeight(listOfItems))

def main():
    temp = 400
    changeCounter = 0
    consecutiveAttemptCounter = 0
    iterationCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)

    while True:
        copyList = []
        copyList = proposedChange(listOfItems)

        changeBool = checkChange(listOfItems, copyList, temp)

        if changeBool: changeCounter += 1
        consecutiveAttemptCounter += 1
        if (consecutiveAttemptCounter == 40000) and (changeCounter == 0):
            displayResults(listOfItems)
            break
        # if (consecutiveAttemptCounter == 40000) or (changeCounter == 4000):
        if (consecutiveAttemptCounter == 4000) or (changeCounter == 400):
            print('Attempts: %d\tChanges: %d\t Temperature: %d\t Iterations: %d\t Current Utility: %d' % (consecutiveAttemptCounter, changeCounter, temp, iterationCounter, calculations.calcUtility(listOfItems)))
            temp *= 0.9
            iterationCounter += 1
            changeCounter = 0
            consecutiveAttemptCounter = 0


if __name__ == "__main__":
  main()