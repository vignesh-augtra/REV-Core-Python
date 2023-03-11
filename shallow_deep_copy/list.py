
import copy

list1 = [1, 2, 3]

# list2 = copy.copy(list1)  # list 2 = [1, 2, 3]

list2 = [1, 2, 3]

list1.append(500) # shallow copy
# del list1 # will create a copy - shallow copy


print("list 1 ", list1) 
print("list 2 ", list2)

