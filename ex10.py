str1 = "I am 6'2\" tall "
str2 = ' I am "2\''
print(str1+str2)

fat_cat = """
I'll do a list:
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass
\a a
\b b
\f f
#\ N{uft-8}
\r r
\v v
"""
print(fat_cat)
#
#while True:
#    for i in ["/","-","|","\\","|"]:
#        print("%s\r"%i)

for i in ["/", "-", "|", "\\", "|"]:
                print("%s\r" % i)

for a in [1, 2, 3, 5, 6]:
    print(a)
for c in ["ab", "cd"]:
    print(c)