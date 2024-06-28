import os
from unittest.mock import patch
import pytest
from src.main import (
    Category,
    Product,
    data_to_class_category,
    data_to_class_product,
    get_json_data,
)

current_dir = os.path.dirname(os.path.abspath(__file__))
path_to_json = os.path.join(current_dir, "../data", "products.json")


@pytest.fixture
def category_fruits():
    return Category(
        "Fruits", "Fruits from Panama", ["avocado", "banana", "dragon-fruit", "mango"]
    )


def test_category(category_fruits):
    assert category_fruits.name == "Fruits"
    assert category_fruits.description == "Fruits from Panama"
    assert category_fruits.products == ["avocado", "banana", "dragon-fruit", "mango"]


@pytest.fixture
def product():
    return Product("Banana", "Mini Bananas from Panama", 2.0, 2000)


def test_product(product):
    assert product.name == "Banana"
    assert product.description == "Mini Bananas from Panama"
    assert product.cost == 2.0
    assert product.count == 2000


@pytest.fixture
def json_file():
    data = [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации,"
            " но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "name": "Iphone 15",
                    "description": "512GB, Gray space",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "name": "Xiaomi Redmi Note 11",
                    "description": "1024GB, Синий",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "name": "Телевизоры",
            "description": "Современный телевизор, который позволяет наслаждаться просмотром,"
            " станет вашим другом и помощником",
            "products": [
                {
                    "name": '55" QLED 4K',
                    "description": "Фоновая подсветка",
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]
    return data


def test_data_to_class_category(json_file):
    result = [
        "name - Смартфоны, description - Смартфоны, как средство не только "
        "коммуникации, но и получение дополнительных функций для удобства жизни, "
        "products: ['Samsung Galaxy C23 Ultra', 'Iphone 15', 'Xiaomi Redmi Note 11']",
        "name - Телевизоры, description - Современный телевизор, который позволяет "
        "наслаждаться просмотром, станет вашим другом и помощником, products: ['55\" "
        "QLED 4K']",
    ]
    assert data_to_class_category(json_file) == result
    result = []
    assert data_to_class_product([]) == result


def test_data_to_class_product(json_file):
    result = [
        "name - Samsung Galaxy C23 Ultra,description - 256GB, Серый цвет, 200MP "
        "камера,cost - 180000.0,count - 5",
        "name - Iphone 15,description - 512GB, Gray space,cost - 210000.0,count - 8",
        "name - Xiaomi Redmi Note 11,description - 1024GB, Синий,cost - 31000.0,count "
        "- 14",
        'name - 55" QLED 4K,description - Фоновая подсветка,cost - 123000.0,count - 7',
    ]
    assert data_to_class_product(json_file) == result
    result = []
    assert data_to_class_product([]) == result


@patch("json.load")
def test_get_json_data(mock_load, json_file):
    mock_load.return_value = json_file
    result = [
        {
            "description": "Смартфоны, как средство не только коммуникации, но и "
            "получение дополнительных функций для удобства жизни",
            "name": "Смартфоны",
            "products": [
                {
                    "description": "256GB, Серый цвет, 200MP камера",
                    "name": "Samsung Galaxy C23 Ultra",
                    "price": 180000.0,
                    "quantity": 5,
                },
                {
                    "description": "512GB, Gray space",
                    "name": "Iphone 15",
                    "price": 210000.0,
                    "quantity": 8,
                },
                {
                    "description": "1024GB, Синий",
                    "name": "Xiaomi Redmi Note 11",
                    "price": 31000.0,
                    "quantity": 14,
                },
            ],
        },
        {
            "description": "Современный телевизор, который позволяет наслаждаться "
            "просмотром, станет вашим другом и помощником",
            "name": "Телевизоры",
            "products": [
                {
                    "description": "Фоновая подсветка",
                    "name": '55" QLED 4K',
                    "price": 123000.0,
                    "quantity": 7,
                }
            ],
        },
    ]
    assert get_json_data(path_to_json) == result


@patch("builtins.open")
def test_get_json_data_file_does_not_exist(mock_open):
    mock_open.side_effect = FileNotFoundError
    assert get_json_data("test_path") == []


def test_new_product_bigger_price():
    product_1 = Product.new_product("avocado", "green avocado from Spain", 30, 2000)
    if product_1:
        product_2 = Product.new_product("avocado", "green avocado from Spain", 35, 500)
        assert (product_2.name, product_2.cost, product_2.count) == ("avocado", 35, 2500)


def test_new_product_smaller_price():
    product_1 = Product.new_product("melon", "green avocado from Spain", 30, 2000)
    if product_1:
        product_3 = Product.new_product("melon", "green avocado from Spain", 15, 300)
        assert (product_3.name, product_3.cost, product_3.count) == ("melon", 30, 2300)
