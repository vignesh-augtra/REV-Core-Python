def find_sum_of_marks(marks_list = []):
    total = 0
    for one_mark in marks_list:
        total += one_mark
    return total

def add_total_mark_to_dict(student_list = []):
    students_list_with_total_mark = []
    for one_student in student_list:
        one_student['total_mark'] = find_sum_of_marks(one_student['marks'])
        students_list_with_total_mark.append(one_student)
    return students_list_with_total_mark

def find_and_show_rank(students_list = []):
    marks_list = []
    sorted_students_list = []
    
    for one_student in students_list:
        marks_list.append(one_student['total_mark'])
    
    marks_list.sort(reverse=True)

    for one_mark in marks_list:
        for one_student in students_list:
            if one_student['total_mark'] == one_mark:
                if one_student not in sorted_students_list:
                    sorted_students_list.append(one_student)
                    break
    return sorted_students_list
                

def show_ranks(students_list = []):
    inital_rank = 1

    print("Name", end="\t\t")
    print("Roll No", end="\t\t")
    print("Rank")
    
    for one_student in students_list:
        print(one_student["name"], end="\t\t")
        print(one_student["roll_no"], end="\t\t")
        print(inital_rank)
        inital_rank += 1

        

    


