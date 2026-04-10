from src.product import Product


class Category:
    name = ""
    description = ""
    __products: list = []
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):

        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):

        if isinstance(product, Product) or issubclass(product.__class__, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self):
        products_out = []

        for prod in self.__products:
            prod_str = f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт."
            products_out.append(prod_str)

        return products_out

    def __str__(self):
        """Вывод строки по print(category)"""

        product_count = 0

        for prod in self.__products:
            product_count += prod.quantity

        res = f"{self.name}, количество продуктов: {product_count} шт."
        return res

    def middle_price(self):
        """ Получение среднего ценника продукции в категории """

        try:
            prod_prices = []

            for product in self.__products:
                prod_prices.append(product.price)

            result = round(sum(prod_prices) / len(prod_prices), 2)
        except ZeroDivisionError as e:
            result = 0

        return result
