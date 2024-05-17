from django.urls import path
from .views import TodoListView, TodoDetailApiView

app_name = 'api-generic'

urlpatterns = [
    path("taskList/", TodoListView.as_view(), name="taskList"),
    path("taskDetail/<int:todo_id>/", TodoDetailApiView.as_view(), name="taskDetail",),
]