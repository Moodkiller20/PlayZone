from django.urls import path
from tictactoe_App import views




urlpatterns = [
    path('', views.tictactoe_view, name='tictactoe'),

]
