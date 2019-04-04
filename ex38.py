ten_thins = "Apples Oranges Corws Thelephone Light Sugar"
stuff = ten_thins.split(' ')
more_stuff = ["Day", "Night", "Song", "Corn"]
while(len(stuff)!=10):
	next_pop = more_stuff.pop()
	print("nextPop:", next_pop)
	stuff.append(next_pop)
	print("Stuff len:", len(stuff))
	
print("stuff:", stuff)
print("[1]:", stuff[1])
print("[-1]:", stuff[-1])
print("pop:", stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:7]))