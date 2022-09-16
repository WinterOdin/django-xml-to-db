from .views import PackageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('package', PackageViewSet, basename="package")
urlpatterns = router.urls
