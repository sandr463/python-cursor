from __future__ import annotations

import time
from abc import abstractmethod, ABC


class Shape:

    def __init__(self):
        self.shape = None


class Color:

    def __init__(self):
        self.color = None


class Figure:
    def __init__(self):
        self.__color: Color = None
        self.__shape: Shape = None
        self.time = None

    def who_i_am(self):
        print(f"My color is {self.__color.color}")
        print(f"My shape is {self.__shape.shape}")
        print(f"My shape is {self.time}")

    def set_color(self, color):
        self.__color = color

    def set_shape(self, shape):
        self.__shape = shape


class Director:

    def __init__(self):
        self._builder = None

    def set_builder(self, input_builder: Builder):
        self._builder = input_builder

    def get_figure(self, custom_builder: Builder = None):
        builder = custom_builder if custom_builder else self._builder

        figure = Figure()

        color = builder.get_color()
        figure.set_color(color)

        shape = builder.get_shape()
        figure.set_shape(shape)

        figure.time = builder.get_creation_time()

        return figure


class Builder(ABC):
    """
    Specify an abstract interface for creating parts of a Product
    object.
    """

    @abstractmethod
    def get_color(self):
        raise NotImplementedError

    @abstractmethod
    def get_shape(self):
        raise NotImplementedError

    @abstractmethod
    def get_creation_time(self):
        raise NotImplementedError


class BlueCircleBuilder(Builder):

    def get_color(self):
        color = Color()
        color.color = "blue"
        return color

    def get_shape(self):
        shape = Shape()
        shape.shape = "Circle"
        return shape

    def get_creation_time(self):
        return time.time()


class RedLineBuilder(Builder):
    def get_color(self):
        color = Color()
        color.color = "red"
        return color

    def get_shape(self):
        shape = Shape()
        shape.shape = "Line"
        return shape

    def get_creation_time(self):
        return time.time()


if __name__ == "__main__":
    director = Director()

    builder = BlueCircleBuilder()
    director.set_builder(builder)

    figure = director.get_figure()

    figure.who_i_am()
    print("Next Figure")
    # director.set_builder(RedLineBuilder())
    figure = director.get_figure(RedLineBuilder())
    figure.who_i_am()