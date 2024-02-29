from typing import List
from project.product import Product


class ProductRepository:

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product):

        self.products.append(product)

    def find(self, product_name: str) -> object or None:

        for product in self.products:

            if product.name == product_name:

                return product

    def remove(self, product_name: str) -> None:

        try:
            self.products.remove(self.find(product_name))
        except ValueError:
            pass

    def __repr__(self):

        return '\n'.join(f"{product.name}: {product.quantity}" for product in self.products)
