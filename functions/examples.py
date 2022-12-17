# def sayGoodMorning(name = "vignesh"):
#     print("Hi", name, "Good Morning!")

# def sayGoodNight(name):
#     print("Hi", name, "Good Night!")

# def sayGoodEvening(name):
#     print("Hi", name, "Good Evening!")

# sayGoodMorning("vignesh")
# sayGoodEvening("vignesh")
# sayGoodNight("vignesh")


def add_numbers(*num_list): 
    sum = 0
    for num in num_list:
        sum += num
    return sum


print(add_numbers(1))
print(add_numbers(6, 7))
print(add_numbers(6, 7, 9))
print(add_numbers(6, 7, 9, 10))



    