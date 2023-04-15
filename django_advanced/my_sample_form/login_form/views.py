from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .custom_model.form_model import LoginForm
def showLoginForm(request):

    template = loader.get_template("login_form.html")

    context = {
        "login_form" : LoginForm()
    }

    return HttpResponse(template.render(context))
