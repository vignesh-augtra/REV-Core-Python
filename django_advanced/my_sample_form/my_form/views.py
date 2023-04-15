from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def sampleText(request):
    # return HttpResponse("Hi from My_form")
    template =  loader.get_template("my_form_template.html")

    return HttpResponse(template.render())
