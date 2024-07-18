from abc import ABC


class BaseCategory(ABC):

    def __str__(self):
        pass


class ZeroCountProductsException(Exception):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Количество товара не может быть нулевым."

    def __str__(self):
        return self.message
