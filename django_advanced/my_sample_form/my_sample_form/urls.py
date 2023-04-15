from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('my_form/', include("my_form.urls")),
    path('login_form/', include("login_form.urls")),

]
