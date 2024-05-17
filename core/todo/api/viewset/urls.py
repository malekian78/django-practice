from rest_framework.routers import DefaultRouter
from .views import TodoView

app_name = "api-viewset"

router = DefaultRouter()
router.register("tasks", TodoView, basename="tasks")
# router.register("taskDetail",TodoDetailApiView,basename="taskDetail",)

urlpatterns = []

urlpatterns += router.urls
