from django.shortcuts import render

# Create your views here.
def slots_view(request):


    return render(request, "slotmachine/slots.html")