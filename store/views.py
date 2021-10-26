from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    if product_count == 1:
        item1 = f'{product_count} Item Found'
        product_count = item1
    else:
        item2 = f'{product_count} Items Found'
        product_count = item2

    context = {
        'products':  products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_datail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_datail.html', context)
