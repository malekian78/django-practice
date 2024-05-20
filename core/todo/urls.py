from django.urls import path, include
from .views import ChangeToDoneOrUnDone, GetWeatherApi, TaskList, customDeleteView, TaskCreate, TaskUpdate #, testingCach

urlpatterns = [
    path('',  TaskList.as_view(), name="task_list"),
    path("create/", TaskCreate.as_view(), name="create_task"),
    path("update/<int:pk>/", TaskUpdate.as_view(), name="update_task"),
    path("complete/<int:pk>/", ChangeToDoneOrUnDone.as_view(), name="DoneUndone_task"),
    path("delete/<int:pk>/", customDeleteView.as_view(), name="delete_task"),
    path("api/apiview/", include("todo.api.apiview.urls")),
    path("api/genericview/", include("todo.api.genericview.urls")),
    path("api/viewset/", include("todo.api.viewset.urls")),
    # path("send_email/", send_email, name="send_email"),
    # path("testing_cach/", testingCach ,name='testingCache'),
    path("getWeather-api/", GetWeatherApi.as_view(), name="getWeatherApi")
]
