from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.views import LoginView


from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
