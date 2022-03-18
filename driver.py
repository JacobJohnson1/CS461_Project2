from pickle import FALSE, TRUE
from numpy import diff
import fileReader
import random
import copy
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
    #print('total utility: %s' % totalUtility)
    #printFunction(listOfItems)

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
    changedItem = random.randint(0, len(listOfItems)-1)
    if copyList[changedItem][2] == 0:
        copyList[changedItem][2] = 1
    elif copyList[changedItem][2] == 1:
        copyList[changedItem][2] = 0
    return(copyList)

#change IS being taken
#lists not being copied correctly
def checkChange(initialList, copyList, temp):
    initialUtility = calcUtility(initialList)
    copyUtility = calcUtility(copyList)
    print('initiallist = %s' % initialUtility)
    print('copylist = %s' % copyUtility)
    difference = (initialUtility - copyUtility)
    probability = exp(-difference / temp)
    if (difference < 0) or (random.random() < probability):
        initialList = copy.deepcopy(copyList)
        print('change accepted!')
        return True
    else: return False

# RESEARCH BEST WAY TO REDUCE TEMP 
def tempReduction(attmeptCounter, changeCounter, temp):
    if (changeCounter == 4000) or (attmeptCounter == 40000):
        temp = (temp * 0.99)

def printFunction(listOfItems):
    print('Packed in car:')
    print('Utility \t Weight')
    for i in range(0, len(listOfItems)-1):
        if listOfItems[i][2] == 1:
            print('%s \t\t %s' % (listOfItems[i][0], listOfItems[i][1]))

def main():
    temp = 40000
    changeCounter = 0
    attemptCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)

    while True:
        tempReduction(attemptCounter, changeCounter, temp)
        copyList = proposedChange(listOfItems)
        changeBool = checkChange(listOfItems, copyList, temp)
        if(changeBool):
            changeCounter += 1
        attemptCounter += 1
        if (attemptCounter == 40000) and (changeCounter == 0):
            break

if __name__ == "__main__":
  main()
