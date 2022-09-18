from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="PyPi API",
        default_version='v1',
        description="An api for newest packages",
        contact=openapi.Contact(email="help@task.com"),
        license=openapi.License(name="Test"),
    ),
    public=True,
)

urlpatterns = [
    path('', include('gathering.urls')),
    path('api/', include('gather_api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger-schema")

]

if settings.ADMIN_ENABLED is True:
    urlpatterns += [path('admin/', admin.site.urls), ]
