import threading
from Scripts import *

if __name__ == "__main__":
    newArray = []
    threadCreateArray = threading.Thread(target=createArray, args=(1000000, newArray))
    threadCreateArray.start()
    threadCreateArray.join()

    treadWriteInFile = threading.Thread(target=writeInFile, args=(newArray, ))
    treadWriteInFile.start()
    treadWriteInFile.join()

    readArray = []
    treadReadFromFile = threading.Thread(target=readFromFile, args=("file.txt", readArray))
    treadReadFromFile.start()
    treadReadFromFile.join()

    treadPrintArray = threading.Thread(target=printArray, args=(readArray, ))
    treadPrintArray.start()
    treadPrintArray.join()