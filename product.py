class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def __str__(self):
        return f"{self.name}, {self.price}, {self.quantity}\n"
    
    def set_quantity(self, new_quantity):
        self.quantity=new_quantity
    
