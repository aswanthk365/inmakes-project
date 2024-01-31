from django.shortcuts import render
from . models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

# Create your views here.

def index(request,c_slug=None):
    c_page=None 
    products=None
    if c_slug != None:
        c_page=get_object_or_404(category,slug=c_slug)
        products=product.objects.all().filter(categorys=c_page,avilabilty=True)
    else:
        products=product.objects.all().filter(avilabilty=True)
    
    #for pagination
    pagination=Paginator(products,10)
    page=request.GET.get('page')
    venues=pagination.get_page(page)
    
    return render(request,'index.html',{'c_page':c_page,'products':venues})

def product_deatails(request,c_slug,pro_slug):
    try :
        deatails=product.objects.get(categorys__slug=c_slug,slug=pro_slug)
    except Exception as e :
        raise e 
    return render(request,'product_deatils.html',{'deatails':deatails})