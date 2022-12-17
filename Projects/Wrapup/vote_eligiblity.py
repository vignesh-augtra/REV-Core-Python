def check_vote_eligiblity():
    try:
        age = int(input("Enter your age : "))
        if age >= 18:
            print("You are eligible to Vote")
        else : 
            print("You are NOT eligible to Vote")
    except Exception as e:
        print("Something went wrong!")
        print(e)