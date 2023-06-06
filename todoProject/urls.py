from django.contrib import admin
from django.urls import path, include

from todoProject.views import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/register', UserRegisterView.as_view(), name='user-register'),
    path('', include('tasks.urls')),
]
