

class Product:
    name = ''
    description = ''
    __price = 0.0
    quantity = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, params: dict):
        res_product = cls(**params)
        return res_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print('Цена не должна быть нулевая или отрицательная!')
        else:
            self.__price = price

    def __add__(self, other):
        """ Сложение сумм всех продуктов в категории"""
        if isinstance(other, self.__class__):
            res = (self.__price * self.quantity) + (other.price * other.quantity)
            return res

        raise TypeError


class Smartphone(Product):
    efficiency = ''
    model = ''
    memory = ''
    color = ''

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country = ''
    germination_period = ''
    color = ''

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
