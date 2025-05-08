from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

def january(request):
    return HttpResponse("This works January!!!")

def february(request):
    return HttpResponse("This works February!!!")

def march(request):
    return HttpResponse("This works March!!!")

def april(request):
    return HttpResponse("This works April!!!")

def may(request):
    return HttpResponse("This works May!!!")

def june(request):
    return HttpResponse("This works June!!!")

def july(request):
    return HttpResponse("This works July!!!")

def august(request):
    return HttpResponse("This works August!!!")

def september(request):
    return HttpResponse("This works September!!!")

def october(request):
    return HttpResponse("This works October!!!")

def november(request):
    return HttpResponse("This works November!!!")

def december(request):
    return HttpResponse("This works December!!!")

def monthly(request, month): # django will pass the same parameter, if use month in urls, then month will be passed in views
    
    challenge_text= ""+ month
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
              'august', 'september', 'october', 'november', 'december']
    if month.lower() not in months:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse("This month of "+challenge_text +" works for me ")