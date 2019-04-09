# class Parent(object):
# 	def implicit(self):
# 		print("PARENT implicit()")
# class Child(Parent):
# 	pass
# dad = Parent()
# son = Child()
# dad.implicit()
# son.implicit()

# class Parent(object):
# 	def override(self):
# 		print("Parent override()")
# class Child(object):
# 	def override(self):
# 		print("Child override()")
# Parent().override()
# Child().override()

# class Parent(object):
# 	def altered(self):
# 		print("Parent altered")
# class Child(Parent):
# 	def altered(self):
# 		print("abd")
# 		super(Child,self).altered()
# 		print("bbc")
# Parent().altered()
# Child().altered()

class Other(object):
	def override(self):
		print("Other over")
	def implicit(self):
		print("Other imp")
	def altered(self):
		print("Other altered")
class Child(object):
	def __init__(self):
		self.other = Other()
	def implicit(self):
		self.other.implicit()
	def override(self):
		print("Child override()")
	def altered(self):
		self.other.altered()
child = Child()
child.implicit()
child.override()
child.altered()