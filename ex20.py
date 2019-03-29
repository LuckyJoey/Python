from sys import argv

script, inputFile = argv

def printAll(f):
    print(f.read())

def rewind(f):
    print(f.seek(0, 0))

def printALine(lineCount, f):
    print("printLine:",lineCount,"  ", f.readline())

currentFile = open(inputFile)

printAll(currentFile)
rewind(currentFile)
printALine(1,currentFile)
rewind(currentFile)
printALine(3,currentFile)