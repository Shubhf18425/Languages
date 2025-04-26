class Person:
    age = 0
    name = "none"
    def __init__(self,newAge = 122,newName="default"):
        self.age = newAge
        self.name = newName

def displayAge(Person):
        print("%s age %d" %(Person.name,Person.age))

person1 = Person(13,"Person2")
person2 = person1
person3 = Person() #--> error --> no default constructor

person1 = Person(888,"Person1")
displayAge(person1)
displayAge(person2)

displayAge(person3)#--> error --> no default constructor


# print()