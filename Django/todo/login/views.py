from django.http import HttpResponse
from django.template import loader

def showWelcomeText(request):
    return HttpResponse("Hello world from Django")


def showGoodByeText(request):
    template = loader.get_template("bye.html")
    context = {
        "message" : "Hi from Django",
        "gender":"male",
        "mark":95, # 35, 70, 90,
        "age":12,
        "nationality":"indian",
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
