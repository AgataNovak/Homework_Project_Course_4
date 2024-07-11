import json
import os
from unittest.mock import patch

import pytest

from src.utils_json_data import get_json_data

path_to_json = os.path.abspath("../data/products.json")


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
    return json.dumps(data)


@patch("builtins.open")
def test_get_json_data(mock_open, json_file):
    mock_open.return_value.__enter__.return_value.read.return_value = json_file
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
    assert get_json_data(os.path.abspath("../data/products.json")) == result


def test_get_json_data_file_not_found():
    assert get_json_data("test_path") == []
