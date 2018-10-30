import copy
from utils.task_2 import uppercase_list
from utils.task_3 import filter_and_load
from utils.task_4 import filter_o_left
from utils.task_5 import sum_min_max
from utils.task_6 import sort_len_name

members = [
    {'age': 43, 'name': 'Denis'},
    {'age': 49, 'name': 'Roman'},
    {'age': 36, 'name': 'Godzilla'},
    {'age': 47, 'name': 'Spike'},
    {'age': 31, 'name': 'SuperMan'},
    {'age': 49, 'name': 'Batman'},
    {'age': 37, 'name': 'Claus'},
    {'age': 55, 'name': 'Frank'},
    {'age': 83, 'name': 'Homer'}
]

print('Task 2')
print("members:      ", members)
members_task2 = copy.deepcopy(members)
print('Task 2 members:', uppercase_list(members_task2))
print('\n')
print('Task 3')
members_task3 = copy.deepcopy(members)
print('Task 3 members:', filter_and_load(members_task3))
print('\n')
print('Task 4')
members_task4 = copy.deepcopy(members)
print('Task 4 members:', filter_o_left(members_task4))
print('\n')
print('Task 5')
members_task5 = copy.deepcopy(members)
print('Task 5 members:', sum_min_max(members_task5))
print('\n')
print('Task 6')
members_task6 = copy.deepcopy(members)
print('Task 6 members:', sort_len_name(members_task6))
print('\n')
