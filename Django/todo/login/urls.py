from . import views
from django.urls import path

urlpatterns = [
    path("welcome/", views.showWelcomeText),
    path("bye/", views.showGoodByeText),
    path("form/", views.formHandling),
]
