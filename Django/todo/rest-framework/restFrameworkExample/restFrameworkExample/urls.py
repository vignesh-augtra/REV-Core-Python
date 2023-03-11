from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.urls import path
import csv

@api_view(['GET'])
def sampleGetRequest(request):
    return JsonResponse({
        "message":"Hello World!"
    })

@api_view(['POST'])
def greet(request):
    inputData = request.data
    name = inputData["name"]
    city = inputData["city"]
    messageString = "Hi " + name + ", you are from " + city
    return JsonResponse({
        "message":messageString
    })

@api_view(['POST'])
def write_toc_csv(request):
    inputData = request.data["usersList"]

    with open("users.csv", "w", newline="") as csvFile:
        writerObject = csv.writer(csvFile)
        writerObject.writerow(["S.No", "Name"])
        writerObject.writerows(inputData)
    
    return JsonResponse({
        "message" : "Write Success"
    })



@api_view(["GET"])
def readFromCsv(request):
    with open("users.csv", "r") as csvFile:
        dataFromCsv = csv.DictReader(csvFile)
        return JsonResponse({
            "data":list(dataFromCsv)
        })


urlpatterns= [
    path("sample_get_request", sampleGetRequest),
    path("greet_user", greet),
    path("csv_write", write_toc_csv),
    path("csv_read", readFromCsv),
]