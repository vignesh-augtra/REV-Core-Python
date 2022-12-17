class Father:
    def __init__(self,familyName, fatherName):
        self.familyName = familyName
        self.name = fatherName
    
    def swimming(self):
        return "Super"

    def getFamilyName(self):
        return self.familyName

    def getName(self):
        return self.name