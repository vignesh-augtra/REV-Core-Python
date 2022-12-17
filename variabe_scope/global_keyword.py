global name 
name =  "vignesh"

print("1.",name)

def changeName():
    global name
    name = "Rakesh"
    print("2.",name)

changeName()

print("3.",name)
