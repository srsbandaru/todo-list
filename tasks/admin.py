from django.contrib import admin
from tasks.models import Task

# Register your models here.
class AdminTask(admin.ModelAdmin):
    list_display = ("title", "task_owner")
    
admin.site.register(Task, AdminTask)