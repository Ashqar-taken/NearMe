from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Intro(request):
    return render(request, "intro.html")

def MAP(request):
    return render(request, 'map.html')

def royapuram(request):
    return render(request, 'roy.html')

def vyaserpadi(request):
    return render(request, "vyaser.html")

def tondiarpet(request):
    return render(request, "tond.html")

def perambur(request):
    return render(request, 'perm.html')

def ayanavaram(request):
    return render(request, 'ayan.html')

def eggmore(request):
    return render(request, 'egg.html')