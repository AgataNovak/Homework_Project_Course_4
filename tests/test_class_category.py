import pytest

from src.class_category import Category
from src.class_product import Product


@pytest.fixture
def category_fruits():
    return Category(
        "Fruits", "Fruits from Panama", ["avocado", "banana", "dragon-fruit", "mango"]
    )


@pytest.fixture
def vegetable_product():
    return Product("tomato", "very red one", 8, 10000)


def test_category(category_fruits):
    assert category_fruits.name == "Fruits"
    assert category_fruits.description == "Fruits from Panama"
    assert category_fruits.products == ["avocado", "banana", "dragon-fruit", "mango"]
    assert str(category_fruits) == "Fruits, количество продуктов: 4"
    assert len(category_fruits) == 4


# def test_add_categories(category_fruits, vegetable_product):
#     assert category_fruits + vegetable_product == [
#         "avocado",
#         "banana",
#         "dragon-fruit",
#         "mango",
#         Product("tomato", "very red one", 8, 10000),
#     ]
#
