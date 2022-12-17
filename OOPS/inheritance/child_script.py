
from father_script import Father

class Children(Father):
    def __init__(self, familyName, childName, fatherName):
        self.familyName = familyName
        self.childName = childName

        Father.__init__(self, familyName, fatherName) # calling parent class constructor
    
    def swimming(self):
        return "Excellent"

    def getName(self):
        return self.childName 
    
    def getFatherName(self):
        return Father.getName(self)