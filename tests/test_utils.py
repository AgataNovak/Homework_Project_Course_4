import os

import pytest

from src.class_category import Category
from src.utils import (EachProduct, data_to_class_category,
                       data_to_class_product)

path_to_json = os.path.abspath("../data/products.json")


@pytest.fixture
def category_fruits():
    return Category(
        "Fruits", "Fruits from Panama", ["avocado", "banana", "dragon-fruit", "mango"]
    )


@pytest.fixture()
def empty_products_list():
    return Category("nothing", "very nothing", [])


def test_each_product(category_fruits):
    r = EachProduct(category_fruits)
    assert list(r) == ["avocado", "banana", "dragon-fruit", "mango"]


def test_each_product_empty(empty_products_list):
    with pytest.raises(ValueError):
        EachProduct(empty_products_list)


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
    result = ["Смартфоны", "Телевизоры"]
    result_list = data_to_class_category(json_file)
    for i in range(len(result_list)):
        assert (result_list[i]).name == result[i]

    result = []
    assert data_to_class_product([]) == result


def test_data_to_class_product(json_file):
    result = [
        "Samsung Galaxy C23 Ultra",
        "Iphone 15",
        "Xiaomi Redmi Note 11",
        '55" QLED 4K',
    ]
    result_list = data_to_class_product(json_file)
    for i in range(len(result_list)):
        assert result_list[i].name == result[i]

    result = []
    assert data_to_class_product([]) == result
