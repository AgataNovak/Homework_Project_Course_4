from src.class_product import Product


class Smartphone(Product):
    """Класс определяющий продукт категории Смартфоны"""

    def __init__(
        self, name, description, cost, count, manufacturer, model, memory, color
    ):
        super().__init__(name, description, cost, count)
        self.manufacturer = manufacturer
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            f"\nНазвание - {self.name},\nОписание - {self.description},\nЦена - {self.cost},"
            f"\nКоличество на складе - {self.count},\nПроизводитель - {self.manufacturer},Модель - \n{self.model},"
            f"\nОбъём памяти - {self.memory},\nЦвет - {self.color}"
        )

    def __add__(self, other):
        # if type(other) == type(self):
        if isinstance(other, Smartphone):
            return super().__add__(other)
        raise TypeError("Нельзя складывать товары из разных категорий")


class Grass(Product):
    """Класс определяющий продукт категории Трава Газонная"""

    def __init__(self, name, description, cost, count, country, grow_period, color):
        super().__init__(name, description, cost, count)
        self.country = country
        self.grow_period = grow_period
        self.color = color

    def __str__(self):
        return (
            f"\nНазвание - {self.name},\nОписание - {self.description},\nЦена - {self.cost},"
            f"\nКоличество на складе - {self.count},\nСтрана производитель - {self.country}"
            f"\nСрок прорастания - {self.grow_period},\nЦвет - {self.color}"
        )

    def __add__(self, other):
        # if type(other) == type(self)
        if isinstance(other, Grass):
            return super().__add__(other)
        raise TypeError("Нельзя складывать товары из разных категорий")


smart = Smartphone(
    "Xiaomi something",
    "NOt bad maaaan",
    13000,
    20000,
    "China",
    "Some model",
    128,
    "Grey",
)
something_other = Grass("grass", "grass is green", 15, 13000, "Spain", 3, "dark green")
something_other_2 = Grass(
    "grass me", "grass is too green", 18, 13000, "Spain", 3, "dark green"
)

# print(type(smart))
# print(type(something_other))
#
# print(isinstance(smart, Grass))
# print(isinstance(smart, Smartphone))

# print(something_other_2 + something_other)

# print(smart)
# print(something_other)
# print(something_other_2)
