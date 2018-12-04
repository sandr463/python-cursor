from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Union


class Position(ABC):

    @abstractmethod
    def calc_price(self):
        raise NotImplementedError


class Product(Position):

    def __init__(self, price):
        self.__price = price

    def calc_price(self):
        return self.__price


class Box(Position):

    def __init__(self, products: List[Union[Position, Box]] = None):
        self.__products = products if products is not None else []

    def calc_price(self):
        total_price = 0
        for obj in self.__products:
            total_price += obj.calc_price()
        return total_price

    def add_product(self, product: Union[Position, Box]):
        self.__products.append(product)
        print("add new product to box")


class Order:

    def __init__(self, positions: List[Position]):
        self.__positions = positions

    def total_price(self):
        return sum([x.calc_price() for x in self.__positions])


if __name__ == "__main__":

    apple = Product(price=2)
    lemon = Product(price=5)
    fruit_box = Box()
    fruit_box.add_product(lemon)
    fruit_box.add_product(apple)
    water_box = Box()
    for i in range(1, 3):
        water_box.add_product(Product(price=i))
    fruit_box.add_product(water_box)
    order = Order(positions=[fruit_box])
    print(order.total_price())