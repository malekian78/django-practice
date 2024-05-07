from django.urls import path
from .views import ChangeToDoneOrUnDone, TaskList, customDeleteView, TaskCreate

urlpatterns = [
    path('',  TaskList.as_view(), name="task_list"),
    path("create/", TaskCreate.as_view(), name="create_task"),
    # path("update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", ChangeToDoneOrUnDone.as_view(), name="DoneUndone_task"),
    path("delete/<int:pk>/", customDeleteView.as_view(), name="delete_task"),
]
