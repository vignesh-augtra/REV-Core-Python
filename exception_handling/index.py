def check_voting_eligibility(age):

    if age >= 18:
        print("OK")
    else:
        print("NO")


def get_user_input():
    try:
        try:
            name = (input("Enter Name :"))
        except Exception as e:
            print("Name is not set propely")
        
        try:
            age = int(input("Enter Age :"))
        except Exception as e:
            raise Exception("Age is not valid")
        check_voting_eligibility(age)
    except Exception as error:
        try:
            print(error)
            age = int(input("Enter Age :"))
            check_voting_eligibility(age)
        except Exception as e:
            exit()
        
    
def get_age():
    try:
        age = int(input("Enter Age : "))
        print(age)
    except Exception as error:
        print("in except block")
        print(error)
    else:
        print("In else block")
    finally:
        print("In Finally")



# get_user_input()
get_age()