from itertools import product

from src.product import Product


class Category:
    name = ''
    description = ''
    __products = []
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        products_out = []

        for prod in self.__products:
            prod_str = f'{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.'
            products_out.append(prod_str)

        return products_out


    def __str__(self):
        """ Вывод строки по print(category)"""

        product_count = 0

        for prod in self.__products:
            product_count += prod.quantity

        res = f'{self.name}, количество продуктов: {product_count} шт.'
        return res
