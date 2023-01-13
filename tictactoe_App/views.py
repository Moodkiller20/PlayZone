from django.shortcuts import render

# Create your views here.

def tictactoe_view(request):


    return render(request,"Tictactoe/game.html")
