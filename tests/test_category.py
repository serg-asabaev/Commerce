import pytest
from unicodedata import category

from src.category import Category
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture()
def category_smartphone():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

@pytest.fixture()
def my_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, '2,25 Ггц', \
                      'Galaxy S23 Ultra', '256GB', 'Серый')

@pytest.fixture()
def my_lawn_grass():
    return LawnGrass('Canada Green', 'Газонная трава семена Канада Грин Универсальная 10 кг / Канада Грин Универсальный 10 кг/ Canada Green Universal 10 кг / семена газона райграс, тимофеевка, овсяница'
                     , 6449
                     , 500, 'Canada', 'Июнь, Июль, Август', 'изумрудно-зеленый')

@pytest.fixture()
def my_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init(category_smartphone):
    assert category_smartphone.name == 'Смартфоны'
    assert category_smartphone.description == 'Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни'
    assert category_smartphone.category_count == 1
    assert category_smartphone.product_count == 3


def test_category_count(category_smartphone):
    assert category_smartphone.category_count == 2
    category_tv = Category('Телевизоры',
                           'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                           [])
    assert category_tv.category_count == 3


def test_product_count():
    product1 = Product('Haier 65 Smart TV S4',
                           'Smart TV:	да Размер диагонали, дюймов: 65 Разрешение экрана: 4K (3840x2160) Тип дисплея: HQLED Частота обновления, Гц: 60',
                           64999,
                            20
                           )
    category_tv = Category('Телевизоры',
                           'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                           [product1])

    assert category_tv.product_count == 7

    category_tv_1 = Category('Телевизоры',
                           'Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником',
                           [product1])

    assert category_tv.product_count == 8

def test_products_private(category_smartphone):

    assert category_smartphone.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                             'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                             'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.']

def test_add_product(category_smartphone):
    product1 = Product("Xiaomi Redmi 11", "1024GB, Синий", 31000.0, 14)
    category_smartphone.add_product(product1)

    assert category_smartphone.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                                             'Iphone 15, 210000.0 руб. Остаток: 8 шт.',
                                             'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.',
                                             'Xiaomi Redmi 11, 31000.0 руб. Остаток: 14 шт.']

def test_product_str(category_smartphone):
    assert str(category_smartphone) == 'Смартфоны, количество продуктов: 27 шт.'


def test_add_product_obj_class(my_smartphone, my_lawn_grass, my_product):
    ctg_1 = Category('Тестовая категория', 'для проверки ограничений классов товаров', [])

    ctg_1.add_product(my_smartphone)
    ctg_1.add_product(my_lawn_grass)
    ctg_1.add_product(my_product)

    assert ctg_1.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.',
                              'Canada Green, 6449 руб. Остаток: 500 шт.',
                              'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.']

def test_add_product_obj_class_error():
    ctg_1 = Category('Тестовая категория 1', 'для проверки ограничений классов товаров', [])
    ctg_2 = Category('Тестовая категория 2', 'для проверки ограничений классов товаров', [])

    try:
        ctg_1.add_product(ctg_2)
    except Exception as e:
        assert type(e) == TypeError

def test_get_avg_price(category_smartphone):
    assert category_smartphone.get_avg_price() == 140333.33

def test_get_avg_price_empty():
    test_ctg = Category('Тестовая категория 1', 'для проверки ограничений классов товаров', [])
    assert test_ctg.get_avg_price() == 0
