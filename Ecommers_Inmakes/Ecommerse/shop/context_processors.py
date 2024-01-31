from . models import category

def category_links(request):
    links=category.objects.all()
    return dict(links=links)

# def products_links(request):
#     product_links=product.objects.all()
#     return dict(product_links=product_links)

