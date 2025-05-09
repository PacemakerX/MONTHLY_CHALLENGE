from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse



challenges = {
    'january': 'Start a daily journal and write one positive thing each day.',
    'february': 'Perform a random act of kindness every week.',
    'march': 'Walk 10,000 steps every day.',
    'april': 'Try a new healthy recipe each week.',
    'may': 'Spend 30 minutes outside every day.',
    'june': 'Read one book by the end of the month.',
    'july': 'Learn a new skill or hobby.',
    'august': 'Declutter one area of your home each week.',
    'september': 'Practice mindfulness or meditation for 10 minutes daily.',
    'october': 'Complete a creative project (e.g., painting, writing, or crafting).',
    'november': 'Write down three things you are grateful for every day.',
    'december': 'Reflect on the year and set goals for the next year.',
}
def monthly_by_name(request, month): # django will pass the same parameter, if use month in urls, then month will be passed in views
    
    if month.lower() not in challenges:
        return HttpResponseNotFound("This month is not supported!")
    
    response_data=f"<h1>{challenges.get(month)}</h1>"
    return HttpResponse(response_data)

def monthly_by_number(request, month):
    if month > 12 or month < 1:
        raise HttpResponseNotFound("This month is not supported!")
    
    month_names = list(challenges.keys())
    month_name = month_names[month - 1]

    redirect_path = reverse("month-challenge", args=[month_name])
    return HttpResponseRedirect(redirect_path)

def monthly_rdirect(request):
    response_data="<ol>"
    for i in challenges:
        response_data += f"<li><a href='{reverse('month-challenge', args=[i])}'>{i.capitalize()}</a></li>"
    response_data+="</ol>"
    return HttpResponse(response_data)
    