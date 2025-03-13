from product import Product
from product_manager import ProductManager
def main():
    list_of_products=[
        Product("Jabuke", 2.55, 11),
        Product("Jaja", 5.6, 10)
    ]
    shop=ProductManager(list_of_products)
    shop.add_products(Product("Ulje", 7.79, 12))
    shop.add_products(Product("Sapun", 3.54, 33))
    shop.all_products()
    print("Ukupna vrednost je: ", shop.price_of_all())

if __name__=="__main__":
    main()