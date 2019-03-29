from sys import exit

def goldRoom():
    print("goldRoom")
    choice = input(">")

    if "0" in choice or "1" in choice:
        howMuch = input(choice)
    else:
        dead("Man,Learn to type a number")



def dead(arg):
    print(arg)
    exit(1)

goldRoom()