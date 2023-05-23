class Product:
    

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.products = []

    
    def add_product(self, product):
        self.products.append(product)

    
    def find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    
    def find_product_by_price(self, price):
        for product in self.products:
            if product.price == price:
                return product
        return None
