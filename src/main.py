import os

from src.class_category import Category
from src.class_product import Product
from src.products_categories_classes import Grass, Smartphone
from src.utils import (EachProduct, data_to_class_category,
                       data_to_class_product)
from src.utils_json_data import get_json_data

path_to_json = os.path.abspath("../data/products.json")

json_data = get_json_data(
    path_to_json
)  # Получение данных о категориях и товарах из JSON файла

product = Product("melon", "something about melon", 5, 1000)
category = Category("fruits", "something about fruits", ["melon", "apples"])

json_categories = data_to_class_category(
    json_data
)  # Создание объектов классов Category и Product из данных JSON файла
json_products = data_to_class_product(json_data)

products_iterator = EachProduct(
    category
)  # Создание объекта итератора при помощи класса EachProduct
for each_category in products_iterator:
    print(each_category)

for each_category in json_categories:  # Итерация по категориям из JSON файла
    products_iterator = EachProduct(each_category)
    for each_product in products_iterator:
        print(each_product)

first_smartphone = Smartphone(
    "Xiaomi something", "something about it", 13000, 20000, "China", "X5", 128, "white"
)

first_grass = Grass(
    "Royal Carpet", "Something about it", 25, 1000, "Spain", 3, "Dark Green"
)
second_grass = Grass(
    "Little granny", "Something about it", 5, 80000, "Belarus", 8, "Light Green"
)

print(first_grass + second_grass)  # Успешное сложение товаров из одной категории

print(first_grass + first_smartphone)  # Ошибка сложения разных категорий
