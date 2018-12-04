from abc import ABC, abstractmethod


class Color(ABC):

    @abstractmethod
    def show_my_color(self):
        raise NotImplementedError


class Shape(ABC):

    def __init__(self, color: Color):
        self.__color = color

    @abstractmethod
    def show_my_shape(self):
        raise NotImplementedError

    def show_my_color(self):
        self.__color.show_my_color()


class Circle(Shape):
    def show_my_shape(self):
        print("I am circle")


class Square(Shape):
    def show_my_shape(self):
        print("I am Square")


class Red(Color):
    def show_my_color(self):
        print("I am red")


class Blue(Color):
    def show_my_color(self):
        print("I am blue")


if __name__ == "__main__":
    red_color = Red()
    blue_color = Blue()

    blue_circle = Circle(blue_color)

    blue_circle.show_my_color()
    blue_circle.show_my_shape()
