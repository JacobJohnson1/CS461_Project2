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
        listOfItems[random.randint(0, 400)][2] = 1

def calcUtility(listOfItems):
    totalUtility = 0.0
    for i in range(0, len(listOfItems)):
        if listOfItems[i][2] == 1:
            totalUtility += listOfItems[i][0]
    weight = calcWeight(listOfItems)
    totalUtility = overWeightCheck(listOfItems, totalUtility, weight)
    print(totalUtility)
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
    changedItem = random.randint(0,400)
    if copyList[changedItem][2] == 0:
        copyList[changedItem][2] = 1
    elif copyList[changedItem][2] == 1:
        copyList[changedItem][2] = 0
    return(copyList)

def checkChange(initialList, copyList, temp):
    initialUtility = calcUtility(initialList)
    copyUtility = calcUtility(copyList)
    difference = (initialUtility - copyUtility)
    probability = exp(-difference / temp)
    if (difference < 0) or (random.random() < probability):
        # check if this is the desired type of copy
        initialList = copyList
        return TRUE
    else: return FALSE

# RESEARCH BEST WAY TO REDUCE TEMP 
def tempReduction(attmeptCounter, changeCounter, temp):
    if (changeCounter == 4000) or (attmeptCounter == 40000):
        temp = (temp * 0.99)

def main():
    temp = 40000
    changeCounter = 0
    attemptCounter = 0
    listOfItems = fileReader.formatInput()
    initialSolution(listOfItems)

    while (attemptCounter != 40000) and (changeCounter != 0):
        tempReduction(attemptCounter, changeCounter, temp)
        copyList = proposedChange(listOfItems)
        changeBool = checkChange(listOfItems, copyList, temp)
        if(changeBool):
            changeCounter += 1
        attemptCounter += 1

if __name__ == "__main__":
  main()
