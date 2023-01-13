from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import  *

# Create your views here.
@login_required(login_url='register')
def homeView(request):
    games = PlayZoneGame.objects.all()
    context ={
        "games":games
    }
    return render(request, 'playzone/index.html',context)
