from django.http import HttpResponse
from django.template import loader
from django import forms
from django.db import connection

def showWelcomeText(request):
    return HttpResponse("Hello world from Django")


def showGoodByeText(request):
    template = loader.get_template("bye.html")
    cursor = connection.cursor()

    # insertion (creation)
    # userName = "Muqthar"
    # password = "2135646"
    # insertCommand = "insert into users (username, password) values (%s,%s)"
    # cursor.execute(insertCommand, [userName,password])


    # update - Ex 1
    # update_username = "Muthu"
    # update_new_password = "7890"
    # update_new_address = "Coimbatore"
    # updateQuery = "update users set password = %s, address=%s where username = %s"
    # cursor.execute(updateQuery, [update_new_password, update_new_address, update_username])

    # update - Ex 2
    # update_ex2_id = "5"
    # new_username = "Sri Mukesh"
    # update_ex2_command = "update users set username = %s where id = %s"
    # cursor.execute(update_ex2_command, [new_username, update_ex2_id])

    # delete 
    # delete_username = "Muqthar"
    # delete_command = "Delete from users where username = %s"
    # cursor.execute(delete_command, [delete_username])

    # Selecting (Read)
    # login_username = "vignesh"
    # login_password = "12345"
    cursor.execute("select username, password, address from users") # reading all records
    # cursor.execute("select username, password from users where username LIKE 'M%'") # reading records that has username which start with M
    # cursor.execute("select username, password from users where username = %s and password = %s", [login_username, login_password]) # reading one record that matches the given username and password
    dataFromUsersTable = list(cursor.fetchall())
    print(dataFromUsersTable)
    context = {
        "message" : "Hi from Django",
        "gender":"male",
        "mark":95, # 35, 70, 90,
        "age":12,
        "nationality":"indian",
        "usersFromDB" : dataFromUsersTable,
        "students":["vignesh", "karthik"],
        "studentName" : "vignesh",
        "trainers": [
        {
        "name":"Vignesh",
        "city":"Cbe"
        },
        {
        "name":"Karthik",
        "city":"Chennai"
        },
        {
        "name":"Naveen",
        "city":"Erode"
        }
        ]
    }
    return HttpResponse(template.render(context))

def formHandling(request):
    template = loader.get_template("form.html")
    context = {
        "username" : forms.CharField()
    }
    return HttpResponse(template.render())
