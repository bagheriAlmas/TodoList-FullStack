from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskView

router = DefaultRouter()
router.register(r'',TaskView,basename='tasks')

urlpatterns = [
    path('tasks/', include(router.urls))
]
