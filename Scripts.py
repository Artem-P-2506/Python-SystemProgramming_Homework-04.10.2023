def createArray(size, newArray):
    for i in range(size):
        newArray.append(i)

def writeInFile(array):
    with open("file.txt", 'w') as file:
        for item in array:
            file.write(str(item) + ",")

def readFromFile(path, readArray):
    with open(path, 'r') as file:
        data = file.read()
        for item in data.split(','):
            readArray.append(item)

def printArray(array):
        countOfNumbersInOneLine = 10
        i = 0
        for item in array:
            print(f"{str(item)}, ", end="")
            i += 1
            if i >= countOfNumbersInOneLine:
                i = 0
                print()