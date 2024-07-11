import pytest

from src.products_categories_classes import Grass, Smartphone


@pytest.fixture
def smartphone_product():
    product = Smartphone(
        "Xiaomi something",
        "NOt bad maaaan",
        13000,
        20000,
        "China",
        "Some model",
        128,
        "Grey",
    )
    return product


@pytest.fixture
def grass_product():
    product = Grass("grass", "grass is green", 15, 13000, "Spain", 3, "dark green")
    return product


@pytest.fixture
def other_grass_product():
    product = Grass("other grass", "grass is green", 20, 1000, "Italy", 5, "dark green")
    return product


def test_smartphone_class(smartphone_product):
    assert smartphone_product.name == "Xiaomi something"
    assert smartphone_product.description == "NOt bad maaaan"
    assert smartphone_product.cost == 13000
    assert smartphone_product.count == 20000
    assert smartphone_product.manufacturer == "China"
    assert smartphone_product.model == "Some model"
    assert smartphone_product.memory == 128
    assert smartphone_product.color == "Grey"


def test_grass_class(grass_product):
    assert grass_product.name == "grass"
    assert grass_product.description == "grass is green"
    assert grass_product.cost == 15
    assert grass_product.count == 13000
    assert grass_product.country == "Spain"
    assert grass_product.grow_period == 3
    assert grass_product.color == "dark green"


def test_add_same_categories(grass_product, other_grass_product):
    assert grass_product + other_grass_product == 215000


def test_add_different_categories(grass_product, smartphone_product):
    with pytest.raises(TypeError):
        grass_product + smartphone_product
