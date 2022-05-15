from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).owner = request.user
            form.save()
        messages.success(request, 'New Task added')
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.filter(owner=request.user)
        paginator = Paginator(all_tasks, 5)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, 'todolist.html', {'all_tasks':all_tasks} )

@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed!")
    return redirect('todolist')

@login_required
def edit_task(request,task_id):
    if request.method == "POST":
        task_object = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task_object)
        if form.is_valid():
            form.save()
        messages.success(request, "Task Edited")
        return redirect('todolist')
    else:
        task_object = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_object':task_object})

@login_required
def mark_task(request, task_id):
    task = TaskList.objects.get(pk = task_id)
    if task.owner == request.user:
        if task.done == True:
            task.done = False
            task.save()
        else:
            task.done = True
            task.save()
    else:
        messages.error(request, "Access Restricted, You Are Not Allowed!")

    return redirect('todolist')

def index(request):
    context = {'index_text':'Welcome to Index page'}
    return render(request, 'index.html', context )

def contact(request):
    context = {'contact_text':'Welcome to contact page'}
    return render(request, 'contact_us.html', context )

def about(request):
    context = {'about_text':'Welcome to about page'}
    return render(request, 'about_us.html', context )
