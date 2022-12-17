a1 = 7
a2 = 7
a3 = '7'
print("{0} is {1} = {2}".format(a1, a2, a1 is a2))
print("{0} is {1} = {2}".format(a1, a3, a1 is a3))

b1 = 'python'
b2 = 'Python'
print("{0} is {1} = {2}".format(b1, b2, b1 is b2))

list = [1, 2, 3]
list = [1, 2, 3]
print("List {0} is {1} = {2}".format(list, list, list is list))

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3, 4)
print("Tuple {0} is {1} = {2}".format(tuple1, tuple2, tuple1 is tuple2))


