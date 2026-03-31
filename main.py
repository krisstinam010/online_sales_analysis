from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

product1 = Product("Laptop", 80000, 5)
product2 = Product("Mouse", 2000, 10)
product3 = Product("Keyboard", 5000, 7)

manager.add_product(product1)
manager.add_product(product2)
manager.add_product(product3)

print("Dostupni proizvodi:")
manager.show_all_products()

print(f"Ukupna vrednost inventara: {manager.total_inventory_value()}")





cart = Cart()

cart.add_to_cart(product1)
cart.add_to_cart(product2)

cart.show_cart()
print("Za naplatu:", cart.total_price())