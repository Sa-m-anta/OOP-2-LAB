class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print(f"Name: {self.name}, Price: ${self.price}")

class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print(f"Warranty: {self.warranty}")

electronic_product = ElectronicProduct("Laptop", 1000, "1 year")
electronic_product.display_detail()