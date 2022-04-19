from pydoc import doc
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('products.urls',namespace='products')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('account/',include('account.urls',namespace='account')),
    path('payment/',include('payment.urls',namespace='payment')),
    path('orders/',include('orders.urls',namespace='orders')),
]

#only used for localhost environment
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)