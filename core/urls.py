from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gather_api.urls'))
    path('api/', include('gather_api.urls'))
]
