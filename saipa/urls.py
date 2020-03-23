from django.contrib import admin
from django.urls import path, include

from authnz import urls as authnz_urls
from car import urls as car_urls
from utils import urls as util_urls


admin.site.site_header = 'Saipa admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(authnz_urls)),
    path('', include(car_urls)),
    path('', include(util_urls)),
]
