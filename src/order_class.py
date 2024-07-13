from src.class_category import BaseCategory


class Order(BaseCategory):
    """Класс определяющий заказ товара"""

    def __init__(self, name, count, total):
        self.name = name
        self.count = count
        self.total = total

    def __str__(self):
        return (
            f'Заказ товара - "{self.name}", количество - {self.count}'
            f" шт. Общая стоимость заказа - {self.total} руб."
        )


# order_1 = Order('product', 120, 12000)
# print(order_1)
