numbers = list(range(7)) # [1, 2, 3, 4,5]
sum = 0

for number in numbers:
    if number == 2:
        continue
    if number == 4:
        break
    sum += number 
else:
    print("sum in else = {}".format(sum))

print("sum at end = {}".format(sum))


# sum = sum + number
# 1st : number = 1; sum = 0
# sum = sum + num // sum = 0 + 1
# sum = 1

# 2nd time : number = 2; sum = 1
# 1 + 2 // sum = 3