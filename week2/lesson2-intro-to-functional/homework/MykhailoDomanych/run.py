from utils.task_1 import members
from utils.task_2 import dic_value_upper_case
from utils.task_3 import load_progress
from utils.task_4 import only_o
from utils.task_5 import sum_max_min_age
from utils.task_6 import sort_lenth
from utils.task_adv import int_to_Roman

if __name__ == "__main__":
    import copy

    # Task 1
    print("#####Task 1#####")
    print(members, '\n')

    # Task 2
    print("#####Task 2#####")
    upper_members = copy.deepcopy(members)
    print(dic_value_upper_case(upper_members), "\n")

    # Task 3
    print("#####Task 3#####")
    load_members = copy.deepcopy(members)
    print(load_progress(load_members), "\n")

    # Task 4
    print("#####Task 4#####")
    only_o_members = copy.deepcopy(members)
    print(only_o(only_o_members), "\n")

    # Task 5
    print("#####Task 5#####")
    sum_members = copy.deepcopy(members)
    print(sum_max_min_age(sum_members), "\n")

    # Task 6
    print("#####Task 6#####")
    sorted_members = copy.deepcopy(members)
    print(sort_lenth(sorted_members), "\n")

    # Task Advance
    print("#####Task Advance. The solution was inspired by the code from the internet goo.gl/H5L7VS#####")
    print(int_to_Roman(6), "\n")
    print(int_to_Roman(13), "\n")
