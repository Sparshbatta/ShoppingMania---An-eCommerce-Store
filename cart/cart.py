from ecommerce.settings import CART_SESSION_KEY
from products.models import Product
from decimal import Decimal
from django.conf import settings

class Cart():

    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if settings.CART_SESSION_KEY not in request.session:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart 

    def add(self,product,product_qty):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id]={'price':str(product.price),'qty':str(product_qty)}
        else:
            self.cart[product_id]['qty']=product_qty
        self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['price']=Decimal(item['price'])
            item['qty']=Decimal(item['qty'])
            item['total_price']=item['price']*item['qty']
            yield item
        
    
    def __len__(self):
        return sum(int(item['qty']) for item in self.cart.values())
    
    def get_subtotal_price(self):
        subtotal = sum(Decimal(Decimal(item['price'])*Decimal(item['qty'])) for item in self.cart.values())
        return subtotal
    

    def get_total_price(self):
        subtotal = sum(Decimal(Decimal(item['price'])*Decimal(item['qty'])) for item in self.cart.values())
        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)
        
        return subtotal + shipping
    
    def delete(self,product,qty):
        product_id=str(product)
        product_qty = qty
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def update(self,product,qty):
        product_id=str(product)
        product_qty = qty
        
        if product_id in self.cart:
            self.cart[product_id]['qty'] = product_qty
            self.save()

    def save(self):
        self.session.modified = True
    

    def clear(self):
        del self.session[settings.CART_SESSION_KEY]
        self.save()




 