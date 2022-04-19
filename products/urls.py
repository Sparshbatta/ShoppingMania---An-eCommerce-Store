from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.products_list,name='home'),
    path('product/<slug:slug>/',views.product_detail,name='product-detail'),   
    path('shop/<slug:category_slug>/',views.category_list,name='category_list'),

]