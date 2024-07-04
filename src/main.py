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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)}"

    def __len__(self):
        return len(self.__products)

    @property
    def products(self):
        return self.__products


class Product:
    """Класс определяющий свойства товаров"""

    name: str
    description: str
    cost: float
    count: int
    list_of_products = []

    def __init__(self, name, description, cost, count):
        self.name = name
        self.description = description
        self.count = count
        self.__cost = cost
        Product.list_of_products.append(
            {"name": self.name, "cost": self.__cost, "count": self.count}
        )

    def __str__(self):
        return f"{self.name}, {self.__cost} руб. Остаток: {self.count} шт."

    def __len__(self):
        return self.count

    def __add__(self, other):
        sum_of_products = (self.__cost * self.count) + (other.__cost * other.count)
        return sum_of_products

    @classmethod
    def new_product(cls, name, description, cost, count):
        for i in range(len(Product.list_of_products)):
            if name == Product.list_of_products[i]["name"]:
                old_product = Product.list_of_products.pop(i)
                if old_product["cost"] > cost:
                    return cls(
                        name,
                        description,
                        old_product["cost"],
                        count + old_product["count"],
                    )
                return cls(name, description, cost, count + old_product["count"])
        return cls(name, description, cost, count)

    @property
    def cost(self):
        """Функция возвращает цену выбранного экземпляра"""

        return self.__cost

    @cost.setter
    def cost(self, cost):
        """Функция принимает новую цену и присваивает её выбранному экземпляру"""

        if self.__cost > cost:
            if (
                input(
                    "Вы собираетесь понизить цену! Подтвердите операцию: Y-да N-нет   "
                ).lower()
                == "y"
            ):
                self.__cost = cost
                return
            else:
                print("Операция изменения цены отменена.")
                return
        else:
            self.__cost = cost
            return

    @cost.deleter
    def cost(self):
        """Функция удаляет свойство цены у выбранного экземпляра"""

        self.__cost = None


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
            return self.products[self.current_value]
        else:
            raise StopIteration


def get_json_data(path_to_json):
    """Функция получения данных из JSON файла"""

    try:
        with open(path_to_json, "r") as json_data_file:
            data = json.load(json_data_file)
            return data
    except FileNotFoundError:
        return []


def data_to_class_category(data):
    """Функция читает файл JSON, и создаёт объекты класса Category"""

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
            product.display = (
                f"name - {product.name},"
                f"description - {product.description},"
                f"cost - {product.cost},"
                f"count - {product.count}"
            )
            products.append(product.display)
    return products
