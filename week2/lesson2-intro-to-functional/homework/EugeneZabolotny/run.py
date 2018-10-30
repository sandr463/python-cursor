from utils.task_1 import members as MEMBERS
from utils.task_2 import name_to_upper
from utils.task_3 import age_loader
from utils.task_4 import filter_o_name
from utils.task_5 import age_statistic
from utils.task_6 import sort_by_name_length
from utils.task_7 import decimal_to_roman

if __name__ == "__main__":
    import copy

    print(MEMBERS, '\n')

    # Task 2
    members = copy.deepcopy(MEMBERS)
    name_to_upper(members)
    print('name_to_upper:\n', members, '\n')

    # Task 3
    members = copy.deepcopy(MEMBERS)
    age_loader(members)
    print('age_loader:\n', members, '\n')

    # Task 4
    members = copy.deepcopy(MEMBERS)
    members = filter_o_name(members)
    print('filter_o_name:\n', members, '\n')

    # Task 5
    members = copy.deepcopy(MEMBERS)
    print('age_statistic:\n', age_statistic(members), '\n')

    # Task 6
    members = copy.deepcopy(MEMBERS)
    members = sort_by_name_length(members)
    print('sort_by_name_length:\n', members, '\n')

    # Task 7
    print('decimal_to_roman:')
    decimal_to_roman(6)
    decimal_to_roman(14)
