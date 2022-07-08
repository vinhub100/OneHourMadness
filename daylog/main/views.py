from django.shortcuts import render


def Home(request):
    return render(request, 'main/home.html', {})


def Daylogs(request):
    daylogs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    return render(request, 'main/daylogs.html', {'title': 'Home - DayLog', 'daylogs': daylogs})
