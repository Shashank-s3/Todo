from . import views
from django.urls import include,path

urlpatterns = [
    path("",views.index,name = "index"),
    path("todolist/",views.todolist,name = "todolist"),
    path("delete/<task_id>",views.delate_task,name = "delete_task"),
    path("contact/",views.contact,name = "contact"),
]
