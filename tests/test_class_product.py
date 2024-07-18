import pytest

from src.class_product import Product


@pytest.fixture
def product():
    return Product("Banana", "Mini Bananas from Panama", 2.0, 2000)


@pytest.fixture()
def other_product():
    return Product("Melon", "Sweet Melon from Turkey", 13.0, 300)


def test_product(product, other_product):
    assert product.name == "Banana"
    assert product.description == "Mini Bananas from Panama"
    assert product.cost == 2.0
    assert product.count == 2000
    assert str(product) == "Banana, 2.0 руб. Остаток: 2000 шт."
    assert len(product) == 2000
    assert product + other_product == 7900.0


def test_new_product():
    new_product = Product("strawberry", "Turkey strawberry", 50, 20000)
    assert str(new_product) == "strawberry, 50 руб. Остаток: 20000 шт."


def test_new_product_bigger_price():

    product_1 = Product.new_product("avocado", "green avocado from Spain", 30, 2000)
    if product_1:
        product_2 = Product.new_product("avocado", "green avocado from Spain", 35, 500)
        assert (product_2.name, product_2.cost, product_2.count) == (
            "avocado",
            35,
            2500,
        )


def test_new_product_smaller_price():

    product_1 = Product.new_product("melon", "green avocado from Spain", 30, 2000)
    if product_1:
        product_3 = Product.new_product("melon", "green avocado from Spain", 15, 300)
        assert (product_3.name, product_3.cost, product_3.count) == ("melon", 30, 2300)


def test_add_product(product, other_product):
    assert product + other_product == 7900


def test_delete_cost(product):
    del product.cost
    assert product.cost is None


def test_len_product(product):
    assert len(product) == 2000
