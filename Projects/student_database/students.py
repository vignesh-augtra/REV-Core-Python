def get_student():
    roll_no = int(input("Enter Roll Number :"))
    name = input("Enter Name : ")
    marks = []

    for index in range(1, 4):
        one_subject_mark = int(input("Enter Mark For Sub " + str(index) + " :" ))
        marks.append(one_subject_mark)
    
    student_dict = {
        "roll_no":roll_no,
        "name":name,
        "marks":marks,
    }

    return student_dict


def show_list(students_list = []):
    print("Name", end="\t\t")
    print("Roll No", end="\t\t")
    print("Mark")
    
    for one_student in students_list:
        print(one_student["name"], end="\t\t")
        print(one_student["roll_no"], end="\t\t")
        print(one_student["marks"])
       

        