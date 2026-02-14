import sys
import time


def makeList():
    LIST = []
    try:
        n = int(input("How many elements?\n> "))
        for i in range(1,n+1):
            LIST.append([i,0])
        time_1 = time.time()
        getAllPermutations(LIST)
        print(time.time() - time_1)
    except ValueError as e:
        print("Value Error : ", e)
        sys.exit(0)

def changeDirections(LIST, MI):
    for element in LIST:
        if element[0] > LIST[MI][0]:
            if element[1] == 0:
                element[1] = 1

            elif element[1] == 1:
                element[1] = 0

def swap(LIST, MI):
    if LIST[MI][1] == 0:
        tempElement = LIST[MI-1]
        LIST[MI-1] = LIST[MI]
        LIST[MI] = tempElement
    elif LIST[MI][1] == 1:
        tempElement = LIST[MI+1]
        LIST[MI+1] = LIST[MI]
        LIST[MI] = tempElement


def findLargestMI(LIST):
    MI = None
    foundMI = False
    for i in LIST:
        if i[1] == 0:
            if LIST.index(i) != 0:
                if MI == None:
                    if i[0] > LIST[LIST.index(i) - 1][0]:
                        MI = LIST.index(i)
                        foundMI = True

                elif MI != None:
                    if ( i[0] > LIST[LIST.index(i) - 1][0] ) and ( i[0] > LIST[MI][0] ):
                        MI = LIST.index(i)
                        foundMI = True

        if i[1] == 1:
            if LIST.index(i) != LIST.index(LIST[-1]):
                    if MI == None:
                        if i[0] > LIST[LIST.index(i) + 1][0]:
                            MI = LIST.index(i)
                            foundMI = True

                    elif MI != None:
                        if ( i[0] > LIST[LIST.index(i) + 1][0]) and ( i[0] > LIST[MI][0]):
                            MI = LIST.index(i)
                            foundMI = True

    if not foundMI:
        return foundMI

    return MI

def getAllPermutations(LIST):
    index = 1
    while True:
        printListWithDirections(LIST, index)
        index += 1
        MI = findLargestMI(LIST)
        if isinstance(MI, bool) and MI == False:
            print("#####END#####")
            break;
        changeDirections(LIST, MI)
        swap(LIST, MI)


def printListWithDirections(LIST, index):
    output = ""
    secondPrint = False
    for i in LIST:
        if secondPrint:
            output += (" ")
        else:
            secondPrint = True

        if i[1] == 0:
            output += ("<" + str(i[0]))
        elif i[1] == 1:
            output += (str(i[0]) + ">")

    print(str(index)+ ". " + output)

makeList()
