# class Base():
class Base: #-> this is also coorect way to define class in python
    def __init__(self , name):
        self.name = name 

    def getName(self):
        return self.name

class Child(Base):
    def __init__(self , name , age):
        Base.__init__(self , name)
        self.age = age

    def getAge(self):
        return self.age

class GrandChild(Child):
    def __init__(self , name , age , address):
        Child.__init__(self , name , age)
        self.address = address

    def getAddress(self):
        return self.address
    

g = GrandChild("shubh" , 20 , "IIITL")
print(g.getName() , g.getAge() , g.getAddress())