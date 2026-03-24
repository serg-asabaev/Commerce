import pytest
from unicodedata import category

from src.category import Category
from src.product import Product

@pytest.fixture()
def category_smartphone():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])


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

    assert category_smartphone.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток 5 шт.',
                                             'Iphone 15, 210000.0 руб. Остаток 8 шт.',
                                             'Xiaomi Redmi Note 11, 31000.0 руб. Остаток 14 шт.']

def test_add_product(category_smartphone):
    product1 = Product("Xiaomi Redmi 11", "1024GB, Синий", 31000.0, 14)
    category_smartphone.add_product(product1)

    assert category_smartphone.products == ['Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток 5 шт.',
                                             'Iphone 15, 210000.0 руб. Остаток 8 шт.',
                                             'Xiaomi Redmi Note 11, 31000.0 руб. Остаток 14 шт.',
                                             'Xiaomi Redmi 11, 31000.0 руб. Остаток 14 шт.']

