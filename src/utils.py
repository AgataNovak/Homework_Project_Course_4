from src.class_category import Category
from src.class_product import Product


def data_to_class_category(data):
    """Функция читает файл JSON, и создаёт объекты класса Category"""

    categories = []
    for dict in data:
        products_list = []
        for i in range(len(dict["products"])):
            products_list.append(dict["products"][i]["name"])
        category = Category(dict["name"], dict["description"], products_list)
        categories.append(category)
    return categories


def data_to_class_product(data):
    """Функция читает файл JSON, и создаёт объекты класса Product"""

    products = []
    for dict in data:
        for i in range(len(dict["products"])):
            product = Product(
                dict["products"][i]["name"],
                dict["products"][i]["description"],
                dict["products"][i]["price"],
                dict["products"][i]["quantity"],
            )
            products.append(product)
    return products


class EachProduct:
    """Класс создающий итерацию по списку товаров определённой категории"""

    def __init__(self, category):
        products_quantity = len(category)
        self.products = category.products
        if products_quantity > 0:
            self.stop = products_quantity
        else:
            raise ValueError("Список продуктов данной категории пуст или отсутствует")

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < self.stop:
            self.current_value += 1
            return str(self.products[self.current_value])
        else:
            raise StopIteration
