from django.urls import path
from . import views
app_name='shop'

urlpatterns = [
    path('',views.index,name='index'),
    path('<slug:c_slug>/',views.index,name='product_categ'),
    path('<slug:c_slug>/<slug:pro_slug>/',views.product_deatails,name='product_deatails'),
]
