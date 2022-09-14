from django.shortcuts import render
from rest_framework import viewsets
from gathering.models import Package
from .filters import PackageFilter
from .serializers import PackageSerializer
from .pagination import PackagePagination

class PackageViewSet(viewsets.ViewSet):
    serializer_class = PackageSerializer
    filterset_class = PackageFilter
    pagination_class = PackagePagination
    queryset = Package.objects.all()