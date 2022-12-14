from rest_framework import viewsets
from gathering.models import Package
from .filters import PackageFilter
from .serializers import PackageSerializer
from .pagination import PackagePagination


class PackageViewSet(viewsets.ModelViewSet):
    serializer_class = PackageSerializer
    filterset_class = PackageFilter
    pagination_class = PackagePagination
    # if we use .object.all() we get warning about UnorderedObjectListWarning due to pagination
    queryset = Package.objects.get_queryset().order_by('id')
