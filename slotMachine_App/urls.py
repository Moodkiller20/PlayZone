from django.urls import path
from slotMachine_App import views




urlpatterns = [
    path('', views.slots_view, name='slots'),

]
