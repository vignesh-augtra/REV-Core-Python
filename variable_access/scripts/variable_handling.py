global count
count = 0

def inc():
    global count
    count += 1

def dec():
    global count
    count -= 1

def get():
    global count
    return count