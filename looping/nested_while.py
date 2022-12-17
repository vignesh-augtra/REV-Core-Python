chars = ['a', 'b', 'c']
numbers = [1, 2, 3, 4, 5] # range(1,6)

chars_length = len(chars)
numbers_length = len(numbers)

# num_loop_index, char_loop_index = 0,0
num_loop_index = char_loop_index = 0

while num_loop_index < numbers_length:
    while char_loop_index < chars_length:
        print("{0}, {1}".format(numbers[num_loop_index], chars[char_loop_index]))
        char_loop_index += 1
    num_loop_index += 1
    char_loop_index = 0