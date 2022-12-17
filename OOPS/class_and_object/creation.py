class Dog:
    #attributes
    name = "empty"
    age = 25

    def __init__(self): #constructor
        print("In init")

    #methods
    def talk(self):
        print("in Talk")
    
    def walk(self):
        print("In walk")

dog1 = Dog() # object creation
print(dog1.age)
dog1.talk()
print("----------")
dog2 = Dog() # object creation
print(dog2.name)
dog2.walk()







    