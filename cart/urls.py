from django.urls import path
from . import views

app_name = 'cart'

urlpatterns= [
    path('',views.cart_catalog,name='cart_catalog'),
    path('add/',views.cart_add,name='cart_add'),
    path('delete/',views.cart_delete,name='cart_delete'),
    path('update/',views.cart_update,name='cart_update'),
]