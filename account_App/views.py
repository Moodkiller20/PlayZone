from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.shortcuts import render, redirect

from account_App.forms import PlayZoneRegistrationForm


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'playzone/index.html')
        else:
            print(username, password)
            messages.success(request, ("There was an error loging you in"))
            return redirect('login')
            user = form.get_user()
            login(request, user)
            print("OK")
            return render(request, 'playzone/index.html')
    else:
        return render(request, 'account/login.html')

def register_view(request):
    if request.method == 'POST':
        form = PlayZoneRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return render(request, 'playzone/index.html')
    else:
        form = PlayZoneRegistrationForm()
    return render(request, 'account/register.html', {'form': form})


def loggout_view(request):
    logout(request)
    return render(request, 'account/login.html')