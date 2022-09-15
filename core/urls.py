from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('gathering.urls')),
    path('api/', include('gather_api.urls')),
]
