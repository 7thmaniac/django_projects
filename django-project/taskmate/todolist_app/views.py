from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def todolist(request):
    context = {'todolist_text':'Welcome to Todo List page'}
    return render(request, 'todolist.html', context )

def contact(request):
    context = {'contact_text':'Welcome to contact page'}
    return render(request, 'contact_us.html', context )

def about(request):
    context = {'about_text':'Welcome to about page'}
    return render(request, 'about_us.html', context )
