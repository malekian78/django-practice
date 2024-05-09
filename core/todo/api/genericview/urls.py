from django.urls import path
from .views import TodoListView, TodoDetailApiView

urlpatterns = [
    path("taskList/", TodoListView.as_view(), name="taskList"),
    path("taskDetail/<int:todo_id>/", TodoDetailApiView.as_view(), name="taskDetail",),
]