from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass


class MixinLog:

    def __init__(self):
        self.message = "Добавлен новый продукт"

    def __repr__(self):
        print(self.message)
        return f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.cost}, {self.count})"


class Product(Base, MixinLog):
    """Класс определяющий свойства товаров"""

    name: str
    description: str
    count: int
    list_of_products: list = []

    def __init__(self, name, description, cost, count):
        self.name = name
        self.description = description
        if count >= 0:
            self.count = count
        else:
            raise ValueError("Количество товара не может быть нулевым")
        self.__cost = cost
        Product.list_of_products.append(
            {"name": self.name, "cost": self.__cost, "count": self.count}
        )
        super().__init__()

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


#
# product_1 = Product('product', 'description', 10, 20)
# print(repr(product_1))
