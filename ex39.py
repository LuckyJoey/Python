states = {'Oregon': 'Or', 'Florida': 'FL'}
cities = {'SZ': 'Shenzhen', 'GZ':'Guangzhou'}
cities['NY']='NewYork'
cities['SH'] = 'ShangHai'
print(cities['SZ'])
print(states['Florida'])
#print(cities['BJ'])
print('-'* 20)
print(cities.items())
for city in cities.items():
	print("city:", city	)
	
for abreviated,citys in cities.items():
print("ab:%s , %s" %(abreviated, citys))
print("cd:",cities[abreviated])
	
state = states.get('Texs')
if not state:
 print("Dose Not Exit")
#print("The city for the 'TX' is: %s" % city )
print("not state")

city = cities.get('TX')
print("TX:",city)