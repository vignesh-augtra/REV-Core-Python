
# import math
# from math import ceil
from math import ceil as ceil_div
# Arithmetic Operators
num1 = 5
num2 = 2
sum = num1 + num2
print('{0} + {1} = {2}'.format(num1, num2, sum))

diff = num1 - num2
print('{0} - {1} = {2}'.format(num1, num2, diff))

mul = num1 * num2
print('{0} * {1} = {2}'.format(num1, num2, mul))

div = num1/num2
print('{0} / {1} = {2}'.format(num1, num2, div))

floor_div = num1//num2
print('{0} // {1} = {2}'.format(num1, num2, floor_div))

ceil_div = ceil_div(num1/num2)
print('{0} "ceil div" {1} = {2}'.format(num1, num2, ceil_div))

pow = num1 ** num2
print('{0} ** {1} = {2}'.format(num1, num2, pow))

mod = num1 % num2
print('{0} % {1} = {2}'.format(num1, num2, mod))

