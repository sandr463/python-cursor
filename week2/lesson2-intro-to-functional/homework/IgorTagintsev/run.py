from utils.task_1 import members as M
from utils.task_2 import upper_name
from utils.task_3 import load
from utils.task_4 import name_filter
from utils.task_5 import age
from utils.task_6 import sort_members_by_name_length


if __name__ == "__main__":
    import copy
    print(M, '\n')
#Task_2
    print('This is result of task 2:')
    members = copy.deepcopy(M)
    upper_name(members)
    print(members, '\n')
#Task_3
    print('This is result of task 3:')
    members = copy.deepcopy(M)
    load(members)
    print(members, '\n')
#Task_4
    print('This is result of task 4:')
    members = copy.deepcopy(M)
    members = name_filter(members)
    print(members, '\n')
#Task_5
    print('This is result of task 5:')
    members = copy.deepcopy(M)
    print(age(members), '\n')
#Task_6
    print('This is result of task 6:')
    members = copy.deepcopy(M)
    members = sort_members_by_name_length(members)
    print(members, '\n')