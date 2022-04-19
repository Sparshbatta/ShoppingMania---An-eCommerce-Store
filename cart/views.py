from math import prod
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .cart import Cart
from django.http import JsonResponse
from products.models import Product
from decimal import Decimal

def cart_catalog(request):
    cart = Cart(request)
    return render(request,'products/cart/catalog.html',{'cart':cart})

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product,id=product_id)
        cart.add(product=product,product_qty=product_qty)
        cartqty = cart.__len__()
        response = JsonResponse({'cart_qty':cartqty}); 
        return response
    
def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.delete(product=product_id,qty=product_qty)
        cart_new_qty = cart.__len__()
        cart_total = cart.get_total_price()
        response = JsonResponse({'qty':cart_new_qty,'sub_total':cart_total})
        return response


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id,qty=product_qty)
        product = Product.products.get(id=product_id)
        product_price = Decimal(product.price)
        new_total_price = Decimal(product_price)*Decimal(product_qty)
        cart_new_qty = cart.__len__()
        cart_total = cart.get_subtotal_price()
        cart_grand_total = cart.get_total_price()
        response = JsonResponse({'qty':cart_new_qty,'sub_total':cart_total,'new_total_price':new_total_price,'grand_total_price':cart_grand_total})
        return response



