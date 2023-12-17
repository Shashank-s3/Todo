from django.contrib import admin
from django.urls import path, include
from todo import views as todo_views
urlpatterns = [
    path("", include('todo.urls')),
    path("admin/", admin.site.urls),
    path('todolist/', include('todo.urls')),
    path('account/', include('users_app.urls')),
    path('contact', todo_views.contact, name='contact'),
]

