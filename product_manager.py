class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_all_products(self):
        if not self.products:
            print("Nema dostupnih proizvoda.")
        else:
            for product in self.products:
                product.show_info()

    def total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total
    
def remove_product(self, name):
    self.products = [p for p in self.products if p.name != name]