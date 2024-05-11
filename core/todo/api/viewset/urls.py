from rest_framework.routers import DefaultRouter
from .views import TodoListView, TodoDetailApiView

app_name = "api-viewset"

router = DefaultRouter()
router.register("taskList", TodoListView, basename="taskList")
router.register("taskDetail",TodoDetailApiView,basename="taskDetail",)

urlpatterns = []

urlpatterns += router.urls
