my_set = set([-4343645,1, 2, 2, 2, 3, 4, 5,5])
print(my_set)

# adding 
my_set.add(-2)
print(my_set)

my_set.update([44, 55, 2])
print(my_set)

#discard
# my_set.remove(82)
my_set.discard(82)
print(my_set)

#clearing
my_set.clear()
print(my_set)

del my_set
print(my_set)