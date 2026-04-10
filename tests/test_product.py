import pytest


from src.product import Product, Smartphone, LawnGrass


@pytest.fixture()
def product_iphone():
    return Product('Iphone 17', 'Смартфон Apple iPhone 17 A3520 256Gb пурпурный sim-esim в регионах России', 89999, 20)

@pytest.fixture()
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture()
def my_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, '2,25 Ггц', \
                      'Galaxy S23 Ultra', '256GB', 'Серый')

@pytest.fixture()
def my_lawn_grass():
    return LawnGrass('Canada Green', 'Газонная трава семена Канада Грин Универсальная 10 кг / Канада Грин Универсальный 10 кг/ Canada Green Universal 10 кг / семена газона райграс, тимофеевка, овсяница'
                     , 6449
                     , 500, 'Canada', 'Июнь, Июль, Август', 'изумрудно-зеленый')


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

def test_add(product_iphone, product_samsung):
    assert product_iphone + product_samsung == 2_699_980

def test_smartphone_init(my_smartphone):
    assert my_smartphone.name == 'Samsung Galaxy S23 Ultra'
    assert my_smartphone.description == '256GB, Серый цвет, 200MP камера'
    assert my_smartphone.price == 180000.0
    assert my_smartphone.quantity == 5
    assert my_smartphone.efficiency == '2,25 Ггц'
    assert my_smartphone.model == 'Galaxy S23 Ultra'
    assert my_smartphone.memory == '256GB'
    assert my_smartphone.color == 'Серый'

def test_lawn_grass_init(my_lawn_grass):
    assert my_lawn_grass.name == 'Canada Green'
    assert my_lawn_grass.description == 'Газонная трава семена Канада Грин Универсальная 10 кг / Канада Грин Универсальный 10 кг/ Canada Green Universal 10 кг / семена газона райграс, тимофеевка, овсяница'
    assert my_lawn_grass.price == 6449
    assert my_lawn_grass.quantity == 500
    assert my_lawn_grass.country == 'Canada'
    assert my_lawn_grass.germination_period == 'Июнь, Июль, Август'
    assert my_lawn_grass.color == 'изумрудно-зеленый'


def test_add_obj_class(my_smartphone, my_lawn_grass):

    sm_2 = Smartphone('Iphone 17', 'Смартфон Apple iPhone 17 A3520 256Gb пурпурный sim-esim в регионах России',
                      89999, 20, '1,5 ГГц', 'iPhone 17', '256Gb', 'пурпурный')

    assert sm_2 + my_smartphone == 2699980.0

    lg_2 = LawnGrass('Трава стандартная', 'Тестовый вариант травы', 5300, 100,
                     'Россия', 'Июль-сентябрь', 'Салатовый')

    assert my_lawn_grass + lg_2 == 3754500

def test_add_obj_class_error(my_smartphone, my_lawn_grass):

    try:
        res = my_smartphone + my_lawn_grass
    except Exception as e:
        assert type(e) == TypeError

def test_mixin_log(capsys):
    sm_1 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, '1,7ГГц','Redmi Note 11', '1024GB', 'Синий')
    captured = capsys.readouterr()
    assert captured.out == "Smartphone('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14, '1,7ГГц', 'Redmi Note 11', '1024GB', 'Синий')\n"

    pr_1 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    captured = capsys.readouterr()
    assert captured.out == "Product('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)\n"

    lg_2 = LawnGrass('Трава стандартная', 'Тестовый вариант травы', 5300, 100,
                     'Россия', 'Июль-сентябрь', 'Салатовый')
    captured = capsys.readouterr()
    assert captured.out == "LawnGrass('Трава стандартная', 'Тестовый вариант травы', 5300, 100, 'Россия', 'Июль-сентябрь', 'Салатовый')\n"


def test_zero_quantity(product_iphone):
    """ Тест ошибки нулевого количества """
    with pytest.raises(ValueError, match='Товар с нулевым количеством не может быть добавлен'):
        Product("Iphone 17", "Смартфон Apple iPhone 17 A3520 256Gb пурпурный sim-esim в регионах России",
                          100000, 0)

