import ex24
def break_words(stuff):
    words = stuff.split(' ')
    return words
print(break_words("dfdfd fd  fdf fdsss"))

def sort(w):
    return sorted(w)
print(sort("dfsdaf424"))

pop0= input("pop 0")
print(break_words(pop0).pop(0))

pop_1 = input("pop -1")
print(break_words(pop_1).pop(-1))
print(ex24.add("fd",12))

