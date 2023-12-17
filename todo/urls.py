from . import views
from django.urls import include,path

urlpatterns = [
    path("",views.index,name = "index"),
    path("todolist/",views.todolist,name = "todolist"),
    path("delete/<task_id>",views.delate_task,name = "delete_task"),
    path("edit/<task_id>",views.edit_task,name = "edit_task"),
    path("complete/<task_id>",views.complete_task,name = "complete_task"),
    path("peding/<task_id>",views.pending_task,name = "pending_task"),
    path("contact/",views.contact,name = "contact"),
]
