from copy import deepcopy


class Figure:

    def clone(self):
        return deepcopy(self)

    def __init__(self):
        self.__private_attr = 10

    def get_private_attr(self):
        return self.__private_attr


class Circle(Figure):

    def __init__(self):
        self.name = "Circle"
        super(Circle, self).__init__()

        
if __name__ == "__main__":

    figure_one = Circle()
    figure_two = figure_one.clone()

    print(figure_one.name)
    print(figure_two.name)

    print(figure_one is figure_two)

    fig_2 = Figure()
    print(fig_2.get_private_attr())