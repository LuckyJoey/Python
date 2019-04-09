class Person(object):
	def __init__(self,name):
		print("I am :",name)
class Man(Person):
	def __init__(self,name):
		super(Man,self).__init__(name)
		print("I am Man")
class OldClass:
	def __init__(self):
		print(self)
#zhangsan = Man("Zhangsan")
#lisi = Person("Lisi")
print(type(Person), " ", type(Man), " ", type(OldClass))
oldClass = OldClass()
print(type(oldClass) )