from django import forms
from django.forms import ModelForm
from tasks.models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "details", "due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type":"date"}),
        }
        labels = {
            "title":"Task Title",
            "details":"Task Details",
            "due_date":"Task Due Date",
        }