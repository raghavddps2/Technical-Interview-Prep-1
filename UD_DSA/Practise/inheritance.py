#The object keyword specifies that all classes are children of the object class
class User(object):

    def __init__(self,name,age,aadhar):
        self.name = name
        self.age = age
        self.aadhar = aadhar
    
    def print(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Aadhar :",self.aadhar)

    def incAge(self):
        self.age = self.age + 1

class superUser(User):

    def __init__(self,name,age,aadhar,ninjaLevel):
        super().__init__(name,age,aadhar)
        self.ninjaLevel = ninjaLevel
    
    def print(self):
        super().print()
        print("Ninja levell: ",self.ninjaLevel)
user1 = User("raghav",10,"9599179")
user2 = User("rahul",21,"234455")
user3 = superUser("raghav",12,"234545",2)
user4 = superUser("rahul",34,"345",4)

user1.print()
user2.print()
user3.incAge()
user3.print()
user4.print()