
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.db import connection
from . import views

@api_view(['POST'])
def calculateVotingEligibility(request):

    # {
    #     username : string,
    #     age : number
    # }

    inputData = request.data

    if inputData['age'] >= 18:
        return JsonResponse({
            "message" : "Hi {}, you are eligible to vote".format(inputData['username'])
        })
    else :
        return JsonResponse({
            "message" : "Hi {}, you are not eligible to vote".format(inputData['username'])
        })
    

@api_view(['GET'])
def getMaleUsers(request):
    cursor = connection.cursor()
    query = 'select * from users where gender = %s '
    cursor.execute(query, ['male'])
    resultSet = list(cursor.fetchall())
    responseObject = []
    for oneUser in resultSet:
        responseObject.append({
            "username":oneUser[1],
            "age":oneUser[2],
            "gender":oneUser[3],
            "position":oneUser[4],
            "salary":oneUser[5],
        })


    return JsonResponse({
        "male_users" : responseObject
    })

@api_view(['POST'])
def getUsersByGender(request):
    cursor = connection.cursor()
    query = 'select * from users where gender = %s '
    cursor.execute(query, [request.data['gender']])
    resultSet = list(cursor.fetchall())
    responseObject = []
    for oneUser in resultSet:
        responseObject.append({
            "username":oneUser[1],
            "age":oneUser[2],
            "gender":oneUser[3],
            "position":oneUser[4],
            "salary":oneUser[5],
        })
    return JsonResponse({
        "users" : responseObject
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_voting_eligibility', calculateVotingEligibility),
    path('api/get_male_users', getMaleUsers),
    path('api/get_users_by_gender', getUsersByGender),
    path('show_users/', views.showUsers, name="users"),
]
