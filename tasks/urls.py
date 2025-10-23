from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.IndexView.as_view(), name = "IndexView"),
    path("tasks/", views.TaskList.as_view(), name = "TaskList"),
    path("tasks/details/<int:pk>", views.TaskDetails.as_view(), name = "TaskDetails"),
    path("tasks/create/", views.CreateTask.as_view(), name = "CreateTask"),
    path("tasks/update/<int:pk>", views.UpdateTask.as_view(), name = "UpdateTask"),
    path("tasks/complete/<int:pk>", views.CompleteTask.as_view(), name = "CompleteTask"),
    path("tasks/delete/<int:pk>", views.DeleteTask.as_view(), name = "DeleteTask")
]