from src.product import Product, Smartphone
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    sm_1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, '2,25 Ггц',\
                      'Galaxy S23 Ultra', '256GB', 'Серый')

    print(sm_1.name)
    print(sm_1.description)
    print(sm_1.price)
    print(sm_1.quantity)
    print(sm_1.efficiency)
    print(sm_1.model)
    print(sm_1.memory)
    print(sm_1.color)