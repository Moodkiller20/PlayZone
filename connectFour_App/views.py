from django.shortcuts import render


# Create your views here.
def connectFour(request):
    return render(request, 'App_connectFour/connectFour.html')
