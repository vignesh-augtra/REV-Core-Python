class Dog: 
    message = "I love my dog!"
    def __init__(self, dogName, dogAge): #constructor
        self.name = dogName
        self.age = dogAge

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName


dog1 = Dog("Rodger", 55) # object creation
print("Old Name : ", dog1.getName())
dog1.setName("Puppy")
print("New Name : ", dog1.getName())

print("-----")
dog2 = Dog("A", 55) # object creation
print("Old Name : ", dog2.getName())
dog2.setName("B")
print("New Name : ", dog2.getName())
print("Message : ", dog2.message)









    