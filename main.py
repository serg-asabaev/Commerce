from src.product import Product, Smartphone, LawnGrass
from src.category import Category

if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    sm_1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, '2,25 Ггц',\
                      'Galaxy S23 Ultra', '256GB', 'Серый')

    sm_2 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, '2,25 Ггц', \
                      'Galaxy S23 Ultra', '256GB', 'Серый')

    lg_1 = LawnGrass('Canada Green', 'Газонная трава семена Канада Грин Универсальная 10 кг / Канада Грин Универсальный 10 кг/ Canada Green Universal 10 кг / семена газона райграс, тимофеевка, овсяница', 6449\
                     , 500, 'Canada', 'Июнь, Июль, Август', 'изумрудно-зеленый')

    lg_2 = LawnGrass('Canada Green',
                     'Газонная трава семена Канада Грин Универсальная 10 кг / Канада Грин Универсальный 10 кг/ Canada Green Universal 10 кг / семена газона райграс, тимофеевка, овсяница',
                     6449 \
                     , 500, 'Canada', 'Июнь, Июль, Август', 'изумрудно-зеленый')

    # print(sm_1.name)
    # print(sm_1.description)
    # print(sm_1.price)
    # print(sm_1.quantity)
    # print(sm_1.efficiency)
    # print(sm_1.model)
    # print(sm_1.memory)
    # print(sm_1.color)

    print(lg_1.name)
    print(lg_1.description)
    print(lg_1.price)
    print(lg_1.quantity)
    print(lg_1.country)
    print(lg_1.germination_period)
    print(lg_1.color)


    print(sm_2 + sm_1)
    print(lg_1 + lg_2)

    ctg_1 = Category('Товары', 'Товары из перечня товаров', [])

    ctg_1.add_product(sm_1)

    print(ctg_1.products)

    ctg_1.add_product(lg_1)
    print(ctg_1.products)

    ctg_1.add_product(product1)
    print(ctg_1.products)