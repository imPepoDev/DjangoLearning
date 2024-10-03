from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def my_view(request):
    a1 = 1
    a2 = 2
    r = a1 + a2
    return HttpResponse(f"Nah, i'd win {r}")
def receba(request):
    a1 = 1
    a2 = 2
    r = a1 + a2
    return HttpResponse(f"Recebo {r}x")