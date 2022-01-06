from django.shortcuts import render
from django.contrib.auth.views import LogoutView

# Create your views here.

def home(request):
    return render(request,'main/home.html',{})


def login(request):
    pass

def signup(request):
    pass

class Logout(LogoutView):
    pass

