from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def who_am_i(self):
        raise NotImplementedError


class Circle(Shape):
    def who_am_i(self):
        print(f"I am a true circle. Look {self.__class__.__name__}")


class Line(Shape):
    def who_am_i(self):
        print(f"I am a true Line. Look {self.__class__.__name__}")


SHAPES = {
    "circle": Circle,
    "line": Line,
}


def create_fig(name):
    if name in SHAPES:
        obj = SHAPES.get(name)
    else:
        raise AttributeError("No such fig")
    return obj()


if __name__ == "__main__":
    fig = create_fig("circle")
    fig.who_am_i()

    figure_two = Circle()
    new_line = Line()
    new_line.who_am_i()