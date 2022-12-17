class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_color(self):
        return "The color is " + self.color

    def get_name(self):
        return "The name is " + self.name

jasmine_flower = Flower("Jasmine", "White")
rose_flower = Flower("Rose", "Red")
print(jasmine_flower.get_name())
print(rose_flower.get_name())
print(jasmine_flower.get_color())
print(rose_flower.get_color())

