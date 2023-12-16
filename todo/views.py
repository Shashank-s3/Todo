from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import todo
from todo.form import TaskForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html", {"name" : "Gana"})

def todolist(request):
    print(request.method)
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,("New Task Added!!"))
        return redirect('todolist')
    else:
        all_tasks = todo.objects.all
        print("todolist")
        return render(request, "todolist.html", {'all_tasks': all_tasks})
def delate_task(request, task_id):
    task = todo.objects.get(pk = task_id)
    task.delete()
    return redirect('todolist')

def contact(request):
    return render(request, "contact.html", {"name" : "contact"})