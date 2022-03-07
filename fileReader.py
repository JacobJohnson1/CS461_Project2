import os

def formatInput():
    inputFile = open('Program2Input.txt', 'r')
    inputArray = inputFile.read()
    inputArray = inputArray.split()
    nestedInputArray = []
    nestedInputArray = [inputArray[i:i+2] for i in range(0, len(inputArray), 2)]
    nestedInputArray = [[float(x) for x in lst] for lst in nestedInputArray]
    for i in range(0, len(nestedInputArray)):
        nestedInputArray[i].append(0)
    return(nestedInputArray)