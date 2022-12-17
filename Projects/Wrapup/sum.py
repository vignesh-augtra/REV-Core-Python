def sum():
    try:
        num1 = float(input("Enter number 1 : "))
        num2 = float(input("Enter number 2 : "))
        print("Sum of {} and {} is {}".format(num1, num2, num1+num2))
    except Exception as e:
        print("Something went wrong!")
        print(e)