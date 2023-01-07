"""PlayZone URL Configuration


"""
from django.urls import path
from playzone_App import views

urlpatterns = [
    path('', views.homeView, name='home'),

]
