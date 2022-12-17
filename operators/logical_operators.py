# and
# Truth Table
#   A       B       Result
#   1       0       0       
#   1       1       1
#   0       0       0
#   0       1       0

# or
# Truth Table
#   A       B       Result
#   1       0       1       
#   1       1       1
#   0       0       0
#   0       1       1

num1 = 10
num2 = 50
session_name = "python"

and_check1 = num1 > 20 and num1 == 10 # 0 and 1
print(and_check1)

and_check2 = num1 < 100 and session_name == "python" and num2 == 80
print(and_check2)

or_check1 = num1 > 20 or num1 == 10 # 0 or 1
print(or_check1)

or_check2 = num1 < 100 or session_name == "python" or num2 == 80
print(or_check2)

combine_check1 = num1 > 100 and session_name == "python" or num2 == 80 # 0 or 0
print(combine_check1)

not_ex1 = not(1 != 1)
print(not_ex1)