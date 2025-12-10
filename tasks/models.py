from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    task_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(default=timezone.now, blank=True)
    
    def __str__(self):
        return f"{self.title}"
    
    @property
    def is_overdue(self):
        today = datetime.now().date()
        if self.due_date and today > self.due_date:
            return True
        return False