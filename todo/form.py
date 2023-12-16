from django import forms
from todo.models import todo

class TaskForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['taskname', 'done']
