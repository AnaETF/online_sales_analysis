from product import Product
class ProductManager:
    def __init__(self, products:list):
        self.products=products
        
    def add_products(self,product:Product):
        self.products.append(product)
    
    def all_products(self):
        for p in self.products:
            print(p)
    
    def price_of_all(self):
        return sum(p.price*p.quantity for p in self.products)
 


        