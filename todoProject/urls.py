from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from todoProject.views import UserRegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/register', UserRegisterView.as_view(), name='user-register'),
    path('api/', include('tasks.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
