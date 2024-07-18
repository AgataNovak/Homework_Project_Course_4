from src.base_for_category_and_order import (BaseCategory,
                                             ZeroCountProductsException)
from src.class_product import Product


class Category(BaseCategory):
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

    def avg_price(self):
        price_sum = 0
        try:
            for product in self.__products:
                price_sum += product.price
            average_price = price_sum / len(self.__products)
            return average_price
        except ZeroDivisionError:
            return 0

    @property
    def products(self):
        return self.__products

    def __add__(self, other):
        if isinstance(other, Product):
            if other.count > 0:
                self.__products.append(other)
                return self.__products
            else:
                raise ZeroCountProductsException


# first_category = Category('something', 'about something', ['1', '2'])
# new_product = Product('name', 'description', 13, 2000)
# first_category + new_product
# print(first_category.products)
#
# product_1 = Product('avocado', 'description', 20, 1000)
# product_2 = Product('banana', 'description', 10, 10000)
# product_3 = Product('coconut', 'description', 30, 0)
#
# category_1 = Category('fruits', 'description', [product_1, product_2])
# category_1 + product_3
