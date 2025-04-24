# ------------------------------------------------------------------------------------
class Person(object):
	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def isEmployee(self):
		return False

	def isIIITian(self):
		return False

class Employee(Person):
	def isEmployee(self):
		return True

class IIITian(Employee):
	def getName(self):
		return "IIIT " + self.name

	def isIIITian(self):
		return True


emp = Person("Geek1") # An Object of Person
# print(emp.getName(), emp.isEmployee(),emp.isIIITian())

emp = Employee("Geek2") # An Object of Employee
# print(emp.getName(), emp.isEmployee(),emp.isIIITian())

emp = IIITian("Geek3") # An Object of Employee
# print(emp.getName(), emp.isEmployee(), emp.isIIITian())

# -----------------------------------------------------------------------------------------------------

class person(object):

	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

class Employee( person ):
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post
				person.__init__(self, name, idnumber)

		def display(self):
				print(self.name)
				print(self.idnumber)
				print(self.salary)
				print(self.post)
				
a = Employee('Rahul', 886012, 200000, "Intern")

a.display()



# Python program to demonstrate private members
# of the parent class
class C(object):
	def __init__(self):
			self.c = 21

			# d is private instance variable   #private variable of parent
			self.__d = 42
class D(C):
	def __init__(self):
			self.e = 84
			C.__init__(self)
object1 = D()

# produces an error as d is private instance variable
# print(object1.d)
# print(object1.d)
print(object1.c)