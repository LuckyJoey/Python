from sys import argv
from os.path import exists

script, fromFile, toFile = argv
print("Formfile %s toFile %s" % (fromFile, toFile))
_fromFile = open(fromFile)
fromFileData = _fromFile.read()
print("formFile is %d bytes" % len(fromFileData))

print("toFile path is exist? answer:%r" % exists(toFile))

_toFile = open(toFile, "w+")
_toFile.write(fromFileData)
print("Alright, all done.", _toFile.read())

_fromFile.close()
_toFile.close()



