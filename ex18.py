def print_two(*args):
    arg1, arg2 = args
    print("arg1:%r arg2:%r" % (arg1, arg2))

def print_two_again(arg1, arg2):
    print("print_twoagain:", arg1, arg2)

def print_one( arg ):
    print("print one:%r" % arg)

print_two(12, "abc")
print_two_again("dba", "bbc")
print_one("oneone")