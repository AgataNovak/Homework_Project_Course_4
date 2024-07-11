from src.class_product import Product


class Category:
    """Класс определеяющий категории товаров"""

    name: str
    description: str
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

    def __add__(self, other):
        if isinstance(other, Product):
            self.__products.append(other.name)
            return self.__products


# first_category = Category('something', 'about something', ['1', '2'])
# new_product = Product('name', 'description', 13, 2000)
# first_category + new_product
# print(first_category.products)
