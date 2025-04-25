class Base2(object):
	def __init__(self):
		self.str2 = "Geek2"
		print("Base2")
	def printStr(self):
		print(self.str2)
		

class Base1(object):
	def __init__(self):
		self.str1 = "Geek1"
		print("Base1")
	def printStr(self):
		print(self.str1)


class Derived(Base1, Base2):
	def __init__(self):
		# Calling constructors of Base1
		# and Base2 classes
		Base1.__init__(self)
		Base2.__init__(self)
		print("Derived")
	def printStrs(self):
		print(self.str1, self.str2)


ob = Derived()
ob.printStrs()
ob.printStr()


# Python program to demonstrate
# multiple inheritance


# Base class1
class Mother:
	mothername = ""
	def mother(self):
		print(self.mothername)

# Base class2
class Father:
	fathername = ""
	def father(self):
		print(self.fathername)

# Derived class
class Son(Mother, Father):
	def parents(self):
		print("Mother :", self.mothername)
		print("Father :", self.fathername)

# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
