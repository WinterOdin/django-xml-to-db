from django.urls import path
from .views import main, package_data

urlpatterns = [
    path('', main, name='home'),
    path('search/', package_data, name='package_url')

]
