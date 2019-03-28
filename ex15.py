from sys import argv
script, filename = argv
txt = open(filename)
print("fileName:", filename)
content = txt.read()
print("content:",content)

print("Type the filename again:")
fileAgain = input(">")
txtAgain = open(fileAgain)
print(txtAgain.read())
txtAgain.close()
txt.close()