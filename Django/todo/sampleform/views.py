from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def text(request):
    template = loader.get_template("./templates/form.html")
    return HttpResponse(template.render())