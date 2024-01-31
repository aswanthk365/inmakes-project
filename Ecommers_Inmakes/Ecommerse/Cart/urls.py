from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cartDeatails/',views.cartDeatails,name='cartDeatails'),
    path('cart_min/<int:product_id>/',views.cart_min,name='cart_min'),


]
