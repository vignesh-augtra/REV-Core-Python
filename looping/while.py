numbers = [10, 20, 30, 40, 50, 60]

current_index = 0
sum = 0

while current_index < len(numbers):
    if numbers[current_index] == 20:
        current_index += 1
        continue
    if numbers[current_index] == 40:
        break
    sum += numbers[current_index]
    current_index += 1
else:
    print(sum)

print("Sum at end = {0}".format(sum))