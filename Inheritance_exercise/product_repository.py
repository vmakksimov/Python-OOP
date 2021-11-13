from Inheritance_exercise.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for x in self.products:
            if x.name == product_name:
                return x
        return None

    def remove(self, product_name):
        for x in self.products:
            if x.name == product_name:
                self.products.remove(x)

    def __repr__(self):
        result = ' '

        for product in self.products:
            result += f'{product.name}: {product.quantity}\n'

        return result.strip()



