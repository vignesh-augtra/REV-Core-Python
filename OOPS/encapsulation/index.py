class Father:
    def __init__(self):
        self.name = "velmurugan"
        self.__familyName = "Indian"

class Children(Father):
    def __init__(self):
        Father.__init__(self)
        print(self.name)
        print(self.__familyName)

vignesh = Children()

