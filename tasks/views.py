from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, RedirectView, DeleteView
from tasks.models import Task
from tasks.forms import TaskForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = "tasks/index.html"

class TaskList(ListView):
    template_name = "tasks/task_list.html"
    model = Task
    context_object_name = "task_list"

    def get_queryset(self):
        # Get all the tasks where the status is Created or Updated
        queryset = Task.objects.filter(status__in=["Created","Updated"])
        return queryset
    
class TaskDetails(DetailView):
    template_name = "tasks/task_detail.html"
    model = Task
    pk_url_kwarg = 'pk'
    http_method_names = ['get', 'post']

class CreateTask(CreateView):
    template_name = "tasks/task_form.html"
    context_object_name = "tasks"
    fields = ["title", "details"]
    model = Task
    success_url = reverse_lazy("tasks:TaskList")

    def post(self, request):
        form = TaskForm(request.POST)
        if not form.is_valid():
            context = {"form":form}
            return redirect(request, self.template_name, context)

        obj = form.save(commit=False)
        obj.status = "Created"
        obj.task_owner = self.request.user
        obj.save() 

        messages.success(request, "Task has been created successfully")
        return redirect(self.success_url)
   
class UpdateTask(UpdateView):
    template_name = "tasks/task_form.html"
    fields = ["title", "details"]
    pk_url_kwarg = 'pk'
    model = Task
    context_object_name = "tasks"
    extra_context = {"form_type":"Update"}
    http_method_names = ["get", "post"]
    success_url = reverse_lazy("tasks:TaskList")

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(self.model, id=self.kwargs["pk"])
        form = TaskForm(request.POST, instance=task)
        if not form.is_valid():
            context = {"form":form}
            return redirect(request, self.template_name, context)
    
        obj = form.save(commit=False)
        obj.status = "Updated"
        obj.save()

        messages.success(request, "Task has been updated successfully. ")
        return redirect(self.success_url)

class CompleteTask(RedirectView):
    success_url = reverse_lazy("tasks:TaskList")

    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id=self.kwargs["pk"])
        task.status = "Completed"
        task.save()
        return redirect(self.success_url)
    
class DeleteTask(DeleteView):
    template_name = "tasks/task_confirm_delete.html"
    model = Task
    pk_url_kwarg = 'pk'
    context_object_name = "task"
    success_url = reverse_lazy("tasks:TaskList")
    http_method_names = ["get", "post"]
