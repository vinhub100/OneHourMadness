
from django.urls import path
from .views import home, signup

urlpatterns = [
    path('signup', signup, name='main-signup'),
    path('', home, name='main-home'),
]
