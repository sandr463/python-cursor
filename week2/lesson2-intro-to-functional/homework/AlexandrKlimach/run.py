from utils.task_1 import name_uppercase
from utils.task_2 import load_progress
from utils.task_3 import find_letter
from utils.task_4 import return_values
from utils.task_5 import sort_list
from utils.task_advanced import int_to_rm
import copy
import pprint

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

print('\n'
      '*****************\n'
      'Task 1\n'
      'For each member make his name uppercase\n'
      '*****************\n')
members_copy = copy.deepcopy(members)
pprint.pprint(name_uppercase(members_copy))
print('\n'
      '*****************\n'
      'Task 2\n'
      'Each member will be exclude of group after reaching the age of 200 years.\n'
      'Add field "load" for each member, which shows percentage of progress\n'
      '*****************\n')
members_copy = copy.deepcopy(members)
pprint.pprint(load_progress(members_copy))
print('\n'
      '*****************\n'
      'Task 3\n'
      'Left only those members who have letter \'o\' in names.\n'
      '*****************\n')
members_copy = copy.deepcopy(members)
pprint.pprint(find_letter(members_copy))
print('\n'
      '*****************\n'
      'Task 4\n'
      'Write function that return three values\n'
      '*****************\n')
members_copy = copy.deepcopy(members)
pprint.pprint(return_values(members_copy))
print('\n'
      '*****************\n'
      'Task 5\n'
      'Sort members by length of their names. If length of names is equal than sort by age.\n'
      '*****************\n')
members_copy = copy.deepcopy(members)
pprint.pprint(sort_list(members_copy))
print('\n'
      '*****************\n'
      'Task Advanced\n'
      'Function that will convert decimal values to Roman Numerals\n'
      '*****************\n')
pprint.pprint(int_to_rm(30))
pprint.pprint(int_to_rm(1403))
pprint.pprint(int_to_rm(621))
pprint.pprint(int_to_rm(2018))
