from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import todo
from todo.form import TaskForm
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import smtplib
import environ 
from email.mime.text import MIMEText
# Create your views here.

env = environ.Env()
environ.Env.read_env()

def index(request):
    return render(request, "index.html", {"name" : "Gana"})
@login_required
def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.manage = request.user
            instance.save()
            messages.success(request,("New Task Added!!"))
        return redirect('todolist')
    else:
        all_tasks = todo.objects.filter(manage=request.user)
        paginator = Paginator(all_tasks, 7)
        page = request.GET.get('pg')
        all_tasks = paginator.get_page(page)
        return render(request, "todolist.html", {'all_tasks': all_tasks})

@login_required
def delate_task(request, task_id):
    task = todo.objects.get(pk=task_id)
    if task.manage == request.user:
        task.delete()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed."))
    return redirect('todolist')


@login_required
def complete_task(request, task_id):
    task = todo.objects.get(pk=task_id)
    if task.manage == request.user:
        task.done = True
        task.save()
    else:
       messages.error(request,("Access Restricted, You Are Not Allowed.")) 

    return redirect('todolist')

@login_required
def pending_task(request, task_id):
    task = todo.objects.get(pk = task_id)
    task.done = False
    task.save()
    return redirect('todolist')

@login_required
def edit_task(request, task_id): 
    if request.method == 'POST':
        task = todo.objects.get(pk = task_id)
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request,("Task is Updates!!"))
        return redirect('todolist')
        
    else:
        task_obj = todo.objects.get(pk=task_id)
        return render(request, 'edit.html', {"task_obj":task_obj})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        body = name +"/n"+ email
        msg = MIMEText(body)
        msg['Subject'] = request.POST['subject']
        body = name + email +request.POST['message']
        msg['From'] = "sirigiripetshashank3@gmail.com"
        msg['To'] = "sirigiripetshashank3@gmail.com"
        password = env('GMAIL_PASSWORD')
        # "dhmw uska rvoy iymv"
        msg = MIMEText(body)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login("sirigiripetshashank3@gmail.com", password)
            smtp_server.sendmail("sirigiripetshashank3@gmail.com", "sirigiripetshashank3@gmail.com", msg.as_string())
            print('email sent')
        return redirect('login')
    else:
        return render(request, "contact.html", {"name" : "contact"})
