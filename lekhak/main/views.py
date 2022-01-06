from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView
from .forms import SignupForm

# Create your views here.

def home(request):
    return render(request,'main/home.html',{})


def login(request):
    pass

def signup(request):
    if request.method == 'POST':
        return redirect('main-home')
    form = SignupForm()
    return render(request, 'main/signup.html', {'form':form})

class Logout(LogoutView):
    pass

