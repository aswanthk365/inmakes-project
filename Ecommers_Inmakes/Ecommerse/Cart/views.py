from django.shortcuts import render,redirect
from shop . models import *
from . models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404
# Create your views here.

def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart


def add_to_cart(request,product_id):
    products=product.objects.get(id=product_id)
    try:
        cartId=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cartId=Cart.objects.create(cart_id=cart_id(request))
        cartId.save()

    try:
        cart_item=CartItem.objects.get(product=products,cart=cartId)
        if cart_item.quntity < cart_item.product.stock :
            cart_item.quntity+=1
        cart_item.save()

    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(product=products,cart=cartId,quntity=1)
        cart_item.save()
    return redirect('cartDeatails')


def cartDeatails(request):
    tottal=0
    counter=0
    cart_items=None
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for i in cart_items:
            tottal += (i.product.price*i.quntity)
            counter += i.quntity
    except:
        pass
    return render(request,'cart.html',{'cart_items':cart_items,'tottal':tottal,'counter':counter})

def cart_min(request,product_id):
    products=product.objects.get(id=product_id)
    cartId=Cart.objects.get(cart_id=cart_id(request))
    cart_items=CartItem.objects.get(product=products,cart=cartId)

    if cart_items.quntity > 1 :
        cart_items.quntity = cart_items.quntity-1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cartDeatails')
        


    
        

