from django.shortcuts import get_object_or_404, render
from .models import Category, Product

def categories(request):
    return {
        'categories':Category.products.all()
    }

def products_list(request):
    products = Product.products.all()
    return render(request,'products/home.html',{'products':products})


def product_detail(request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request,'products/detail.html',{'product':product})

def category_list(request,category_slug):
    if category_slug=='all':
        products= Product.products.all()
        return render(request,'products/category.html',{'category':'All','products':products})
    else:
        category = get_object_or_404(Category,slug_title=category_slug)
        products = Product.products.filter(category=category)
        return render(request,'products/category.html',{'category':category,'products':products})

    

