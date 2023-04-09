from django.http import HttpResponse
from django.template import loader
from django.db import connection

def showUsers(request):
    template = loader.get_template("users.html")

    cursor = connection.cursor()
    query = 'select * from users where gender = %s '
    cursor.execute(query, ['male'])
    maleUsers = []
    for oneUser in list(cursor.fetchall()):
        maleUsers.append({
            "username":oneUser[1],
            "age":oneUser[2],
            "gender":oneUser[3],
            "position":oneUser[4],
            "salary":oneUser[5],
        })


    cursor.execute(query, ['female'])
    femaleUsers = []
    for oneUser in list(cursor.fetchall()):
        femaleUsers.append({
            "username":oneUser[1],
            "age":oneUser[2],
            "gender":oneUser[3],
            "position":oneUser[4],
            "salary":oneUser[5],
        })

    context = {
        "users_list_1" : maleUsers,
        "users_list_2" : femaleUsers,
        "heading1" : "Male Users",
        "heading2" : "Female Users",
    }
    return HttpResponse(template.render(context))
