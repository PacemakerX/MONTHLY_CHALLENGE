from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


def monthly_by_name(request, month): # django will pass the same parameter, if use month in urls, then month will be passed in views
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
              'august', 'september', 'october', 'november', 'december']
    if month.lower() not in months:
        return HttpResponseNotFound("This month is not supported!")
    
    return HttpResponse("This month of "+month +" works for me ")

def monthly_by_number(request,month):

    if (month>12 or month<1):
        return HttpResponseNotFound("This month is not supported")
    else:
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 
              'august', 'september', 'october', 'november', 'december']
        return monthly_by_name(request,months[month-1])     
