my_list = [10, -9, 30, 40]
print(my_list)
my_list[0] = 5 # update
print(my_list)

#insert
my_list.insert(1, 15)
print(my_list)

#append
my_list.append(25)
print(my_list)

#extend
my_list.extend([1, 2, 3])
print(my_list)

# del - elem
del my_list[1]
print(my_list)

# sort
my_list.sort()
print(my_list)

element = my_list.pop()
print(element)
print(my_list)

my_list.remove(35)
print(my_list)

# del entire list
# del my_list
# print(my_list)