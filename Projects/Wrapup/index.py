import sum
import vote_eligiblity


def options_handler(option):
    try:

        if option == 1:
            sum.sum()
        elif option == 2:
            vote_eligiblity.check_vote_eligiblity()
        elif option == 3:
            exit()
        else:
            print("Invalid Option")

    except Exception as e:
        print("Something went wrong!")
        print(e)


def options():
    try:
        while(True):
            print("1. Sum")
            print("2. Vote")
            print("3. Exit")
            user_chosen_option = int(input("Enter Option : "))
            options_handler(user_chosen_option)

    except Exception as e:
        print("Something went wrong!")
        print(e)


options()
    

    


