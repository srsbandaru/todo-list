from django import forms
from django.forms import ModelForm
from tasks.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "details"]
        labels = {
            "title":"Task Title",
            "details":"Task Details",
        }