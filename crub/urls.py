from django.urls import path
from . import views

#these are essentially routes

urlpatterns = [
    path("", views.home, name= "home")


]