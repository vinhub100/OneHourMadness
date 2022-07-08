from django.urls import path, re_path, include
from .views import Home, Daylogs


urlpatterns = [
    path('daylogs', Daylogs),
    path('', Home),
]
