from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import Task
from django.shortcuts import redirect
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
# from .forms import TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list_tasks.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)
