from django.urls import path
from rockpaperscissor_App import views




urlpatterns = [
    path('', views.rockpaperscissor_view, name='rockpaperscissor'),

]
