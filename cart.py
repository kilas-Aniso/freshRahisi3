class ShoppingCart:
    def __init__(self,quantity,address, payment_method,price,product,category):
        self.products = []
        self.quantity = quantity
        self.adress =address
        self.payment_method = payment_method
        self.price=price
        self.product=product
        self.category = category
    def add_item(self, product):
        # method to add a product to the shopping cart
        self.products.append(product)
    def remove_item(self, product):
        # method to remove a product from the shopping cart
        self.products.remove(product)
    def checkout(self, quantity,category):

        total = category.product.price * quantity
        return total
