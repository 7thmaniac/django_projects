from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import Tasklist

# Create your views here.
def todolist(request):

    all_tasks = Tasklist.objects.all


    return render(request, 'todolist.html', {'all_tasks':all_tasks} )

def contact(request):
    context = {'contact_text':'Welcome to contact page'}
    return render(request, 'contact_us.html', context )

def about(request):
    context = {'about_text':'Welcome to about page'}
    return render(request, 'about_us.html', context )
