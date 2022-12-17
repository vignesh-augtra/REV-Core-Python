student = {
    "name":"vignesh",
    "so_called_name":"vignesh",
    "age":25,
    "languages_know":["sdfsd","sdfsdffsd"],
    1:"One",
    (1, 2, 3):"sdfsdfsdf",
    "education":{
        "HSC":"450",
        "SSLC":"400",
    }
}

print(student)
#accessing
print(student[1])
print(student["age"])
print(student[(1, 2, 3)])
print(student['education']['SSLC'])

student['education']['SSLC'] = "1024"
print(student['education']['SSLC'])

del student['education']['SSLC']
print(student['education'])