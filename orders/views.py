from decimal import InvalidOperation
from django.shortcuts import render
from django.http.response import JsonResponse
from cart.cart import Cart
from decimal import getcontext
from .models import Order, OrderItem

def add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        getcontext().prec=100
        user_id = request.user.id
        user_name = request.POST.get('custName')
        address1 = request.POST.get('custAdd')
        address2 = request.POST.get('custAdd2')
        order_key = request.POST.get('order_key')
        postCode = request.POST.get('postCode')
        cart_total_price = cart.get_total_price()
        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            print(user_id)
            print(user_name)
            print(address1)
            print(address2)
            print(order_key)
            print(postCode)
            print(cart_total_price)
            print(repr(cart_total_price))
            try:
                order = Order.objects.create(user_id=user_id, full_name=user_name,address1=address1,
            address2=address2,post_code=postCode,total_paid=cart_total_price,order_key=order_key)
            except InvalidOperation as e:
                print(e)
            order_id = order.pk
            for item in cart:
                OrderItem.objects.create(order_id=order_id, product=item['product'],price=item['price'],quantity=item['qty'])
        response = JsonResponse({'success':'Order successfully processed'})
        return response
        

def payment_confirmation(data):
    Order.objects.filter(order_key=data).update(billing_status=True)

def user_orders(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders

