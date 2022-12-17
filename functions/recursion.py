def print_1_to_10(num):
    print(num)
    if num <= 10:
        print_1_to_10(num+1)

print_1_to_10(1)
print("The End...")