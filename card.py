from product import Product
class Card:
    def __init__(self, products: list):
        self.products=products
    
    def add_products(self, product:Product):
        self.products.append(product)
        
    def products_price(self):
        return sum(p.price*p.quantity for p in self.products)
    
    def products_in(self):
        for p in self.products:
            print(p)
        