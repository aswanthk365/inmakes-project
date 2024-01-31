from django.urls import path
from . import views
from shop.models import *

urlpatterns = [
    path('search_result/',views.search,name='search_result'),
]
