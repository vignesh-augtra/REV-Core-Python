import os

fileName = "sample1.txt"

if os.path.exists(fileName):
    os.remove(fileName)
else : 
    print("no")