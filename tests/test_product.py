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

def test_new_product():
    product_dict = {
        'name': 'Nokia 3600',
        'description': 'Черный 512 мб.',
        'price': 7390.0,
        'quantity': 100
    }
    product1 = Product.new_product(product_dict)

    assert product1.name == 'Nokia 3600'
    assert product1.description == 'Черный 512 мб.'
    assert product1.price == 7390.0
    assert product1.quantity == 100


def test_price_getter(product_iphone):
    assert product_iphone.price == 89999


def test_price_setter(product_iphone):
    assert product_iphone.price == 89999
    product_iphone.price = 70000.0
    assert product_iphone.price == 70000.0
