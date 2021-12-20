from django.http import HttpResponse
from django.shortcuts import render

def testf(request):
    return HttpResponse('HELLO')

def temp(request):
    param={'NAME':'shraddha'}
    return render(request, 'home.html',param)