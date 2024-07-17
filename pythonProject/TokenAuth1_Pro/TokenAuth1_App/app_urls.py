from django.contrib import admin
from django.urls import path
from .views import CustomUserListView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('customuserlist/', CustomUserListView.as_view()),
    path('api-token-auth/',obtain_auth_token),
]
