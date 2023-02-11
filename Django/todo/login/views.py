from django.http import HttpResponse
from django.template import loader

def showWelcomeText(request):
    return HttpResponse("Hello world from Django")


def showGoodByeText(request):
    template = loader.get_template("bye.html")
    return HttpResponse(template.render())
