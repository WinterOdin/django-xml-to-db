import django_filters
from gathering.models import Package


class PackageFilter(django_filters.FilterSet):
    class Meta:
        model = Package
        fields = {
            'title': ['icontains'],
            'link': ['icontains'],
            'pubDate': ['icontains', 'lte', 'gte'],
            'description': ['icontains'],
            'author': ['icontains'],
        }
