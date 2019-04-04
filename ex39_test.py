import hashmap
import collections
# states = hashmap.new()
# hashmap.set(states, "Oregon", "OR")

cities = hashmap.new()
hashmap.set(cities,"SZ","shenzhen")
hashmap.set(cities, "BJ", "beijing")

print ('-'*10)
#
print("Shenzen:",hashmap.get(cities,"SZ"))
print("Beijing:", hashmap.get(cities, "BJ"))
# print("OR:",hashmap.get(states, "Oregon"))
# print("ABC:", hashmap.get(states, "abc"))

print('-'*10)
hashmap.list(cities)

print("=="*20)
print(hashmap.get(cities, "GZ", "Dont Exit"))

testOrderDict = { }
testOrderDict['1'] = "a"
testOrderDict['3'] = 'dc'
testOrderDict['2'] = 'fc'
new = collections.OrderedDict(sorted(testOrderDict.items()), key=lambda t:t[1])
for k,v in testOrderDict.items():
	print("OrderDict:", k)
for k, v in new.items():
	print("newDict",k)
print("new:",new)