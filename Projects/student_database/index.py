# 1. Students data entry
#     -roll_no (unique)
#     -marks for 5 subjects
#     -name
# 2. list of students
# 3. Find Rank
# 4. Exit

import students
import mark

global students_list
students_list = []

def get_option():
    print("*************************")
    print("1. Add a Student")
    print("2. View all students")
    print("3. Find Rank")
    print("4. Exit")
    print("*************************")

    user_choosed_option = int(input("Enter option : "))   
    return user_choosed_option
    
while(True):
    option = get_option()
    print("user choosed option :", option)

    if option == 1:
        students_list.append(students.get_student())
    elif option == 2:
        students.show_list(students_list)
    elif option == 3:
        students_list_with_total_mark = mark.add_total_mark_to_dict(students_list)
        sorted_list = mark.find_and_show_rank(students_list_with_total_mark)
        mark.show_ranks(sorted_list)
    elif option == 4:
        exit()
    else:
        print("invalid Option. Please Choose correctly!")




