from django.urls import path

from .views import TodoListApiView, TodoDetailApiView

urlpatterns = [
    path("taskList/", TodoListApiView.as_view(), name="taskList"),
    path("taskDetail/<int:todo_id>/",TodoDetailApiView.as_view(),name="taskDetail",),
]