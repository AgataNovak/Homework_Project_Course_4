import json


class Category:
    """Класс определеяющий категории товаров"""

    name: str
    description: str
    products: list
    counted_categories = 0
    counted_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.counted_categories += 1
        Category.counted_products += len(self.products)

    @property
    def products(self):
        return self.__products


class Product:
    """Класс определяющий свойства товаров"""

    name: str
    description: str
    cost: float
    count: int

    def __init__(self, name, description, cost, count):
        self.name = name
        self.description = description
        self.count = count
        self.__cost = cost

    @classmethod
    def new_product(cls, name, description, cost, count):
        return cls(name, description, cost, count)

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, cost):
        self.__cost = cost

    @cost.deleter
    def cost(self):
        self.__cost = None


def get_json_data(path_to_json):
    """Функция получения данных из JSON файла"""

    try:
        with open(path_to_json, "r") as json_data_file:
            data = json.load(json_data_file)
            return data
    except FileNotFoundError:
        return []


def data_to_class_category(data):
    """Функция читает файл JSON и создаёт объекты класса Category"""

    categories = []
    for dict in data:
        products_list = []
        for i in range(len(dict["products"])):
            products_list.append(dict["products"][i]["name"])
        category = Category(dict["name"], dict["description"], products_list)
        category.display = (
            f"name - {category.name},"
            f" description - {category.description},"
            f" products: {category.products}"
        )
        categories.append(category.display)
    return categories


def data_to_class_product(data):
    """Функция читает файл JSON и создаёт объекты класса Product"""

    products = []
    for dict in data:
        for i in range(len(dict["products"])):
            product = Product(
                dict["products"][i]["name"],
                dict["products"][i]["description"],
                dict["products"][i]["price"],
                dict["products"][i]["quantity"],
            )
            product.display = (
                f"name - {product.name},"
                f"description - {product.description},"
                f"cost - {product.cost},"
                f"count - {product.count}"
            )
            products.append(product.display)
    return products


# product_1 = Product('banana', 'from Panama', 25, 1500)
# print(product_1.name)
# print(product_1.cost)
# print(product_1.count)
#
# product_2 = Product.new_product('melon', 'from Panama', 15, 2000)
# print(product_2.name)
# print(product_2.cost)
# print(product_2.count)
#
# product_2.cost = 18
# print(product_2.cost)
#
# del product_2.cost
# print(product_2.cost)
