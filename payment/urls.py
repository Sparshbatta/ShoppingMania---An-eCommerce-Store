from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('',views.CartView,name='paymentCart'),
    path('orderplaced/',views.order_placed,name='order_placed'),
    path('webhook',views.stripe_webhook),
    path('error/',views.Error.as_view(),name='error'),
]
