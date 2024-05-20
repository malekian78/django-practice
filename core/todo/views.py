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
from .forms import TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
# from django.http import HttpResponse
# import time
# from .tasks import sendEmail

# def send_email(request):
#     # time.sleep(3)
#     sendEmail.delay()
#     return HttpResponse("<h1> Done Sending </h1>")
import requests
# from django.http import JsonResponse
# from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from rest_framework.response import Response

# def testingCach(request):
#     print(cache.get("test_delay_api"))
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://338780c3-26ed-48b4-907d-edfb19ce8117.mock.pstmn.io/test/delay/5")
#         cache.set("test_delay_api", response.json())
#     return JsonResponse(cache.get("test_delay_api"))

# @cache_page(60)
# def testingCach(request):
#     response = requests.get("https://338780c3-26ed-48b4-907d-edfb19ce8117.mock.pstmn.io/test/delay/5")
#     return JsonResponse(response.json())

class GetWeatherApi(APIView):
    # Cache page for the requested url
    @method_decorator(cache_page(20 * 60))
    def get(self, request, format=None):
        # showing the weather condition in Isfahan , refresh every 20 minutes
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        api_key = "3e957a497721f45c0a5217969c5b3d9c"
        city = "Isfahan"
        url = base_url + "appid=" + api_key + "&q=" + city
        response = requests.get(url)
        return Response(response.json())
    
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/list_tasks.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title"]
    success_url = reverse_lazy("task_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class ChangeToDoneOrUnDone(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = not object.complete
        object.save()
        return redirect(self.success_url)

class customDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    success_url = reverse_lazy("task_list")
    form_class = TaskUpdateForm
    template_name = "todo/update_task.html"