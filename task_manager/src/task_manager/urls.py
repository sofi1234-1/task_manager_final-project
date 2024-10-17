"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tasks.views import api_root
from tasks.views import TaskList, TaskDetail, TaskComplete, TaskIncomplete, UserList, UserDetail, CustomAuthToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/tasks/', TaskList.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('api/tasks/<int:pk>/complete/', TaskComplete.as_view(), name='task-complete'),
    path('api/tasks/<int:pk>/incomplete/', TaskIncomplete.as_view(), name='task-incomplete'),
    path('api/users/', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('api/auth/token/', CustomAuthToken.as_view(), name='auth-token'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
