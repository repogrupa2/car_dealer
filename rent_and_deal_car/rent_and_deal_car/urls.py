from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include("car_rent.urls")),
    path('accounts/', include('accounts.urls')),
   ]
