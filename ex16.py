from sys import argv
script, filename = argv
print("We are going to erase %r." % filename)
print("if u dont want that ,hit CTRL-C")
print("if you do want that, hit RETURN")
input("?")
print("opening the file...")
target = open(filename, "w+")

print("Trencating the file. goodbye")
target.truncate()

print("Now Im going to ask you for three lines")
line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Im going to write these to the file")
target.write(line1)
target.write("\n")
target.write(line2+"\n"+line3)

print("And finally ,we close it:", target.read())
target.close()

