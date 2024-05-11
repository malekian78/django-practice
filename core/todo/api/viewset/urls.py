from rest_framework.routers import DefaultRouter
from .views import TodoListView

app_name = "api-viewset"

router = DefaultRouter()
router.register("tasks", TodoListView, basename="tasks")
# router.register("taskDetail",TodoDetailApiView,basename="taskDetail",)

urlpatterns = []

urlpatterns += router.urls
