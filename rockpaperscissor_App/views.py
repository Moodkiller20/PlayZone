from django.shortcuts import render

# Create your views here.
def rockpaperscissor_view(request):

    return render(request, 'rockpaperscissor/game.html')