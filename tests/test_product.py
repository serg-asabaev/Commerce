import pytest


from src.product import Product


@pytest.fixture()
def product_iphone():
    return Product('Iphone 17', 'Смартфон Apple iPhone 17 A3520 256Gb пурпурный sim-esim в регионах России', 89999, 20)


def test_init(product_iphone):
    assert product_iphone.name == 'Iphone 17'
    assert product_iphone.description == 'Смартфон Apple iPhone 17 A3520 256Gb пурпурный sim-esim в регионах России'
    assert product_iphone.price == 89999
    assert product_iphone.quantity == 20


def test_name_change(product_iphone):
    assert product_iphone.name == 'Iphone 17'
    product_iphone.name = 'Iphone 17(пурпурный)'
    assert product_iphone.name == 'Iphone 17(пурпурный)'


def test_quantity_change(product_iphone):
    assert product_iphone.quantity == 20
    product_iphone.quantity = 120
    assert product_iphone.quantity == 120