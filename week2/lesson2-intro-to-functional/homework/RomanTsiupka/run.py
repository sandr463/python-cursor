
# Task 2
# For each member make his name uppercase
# Each member will be exclude of group after reaching the age of 200 years.
# Add field "load" for each member, which shows percentage of progress
# members = [
#    {'age': 43, 'name': 'Denis'},
#    {'age': 49, 'name': 'Roman'},
#    {'age': 36, 'name': 'Godzilla'},
#    {'age': 47, 'name': 'Spike'},
#    {'age': 31, 'name': 'SuperMan'},
#    {'age': 49, 'name': 'Batman'},
#    {'age': 37, 'name': 'Claus'},
#    {'age': 55, 'name': 'Frank'},
#    {'age': 83, 'name': 'Homer'}
#     ]
#
# Task 3
# Left only those members who have letter 'o' in names.
#
# Task 4
# Write function that return three values
# 1. Summary age of members.
# 2. The youngest member
# 3. The oldest member.
#
# Task 5
# Sort members by length of their names. If length of names is equal than sort by age.
#
# Advanced
# Task 6
# Write function that will convert decimal values to Roman Numerals

import copy
from utils.task2 import upper_case
from utils.task3 import left_o
from utils.task4 import total_value
from utils.task5 import sort_m
from utils.task6 import solution

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

if __name__ == "__main__":
    print('orig     ', members)
    print('uppercase', upper_case(copy.deepcopy(members)))
    print('\nleft members with "o"', left_o(copy.deepcopy(members)))
    sum_age, min_age, max_age = total_value(members)
    print('\nSummary age :', sum_age, ', youngest member is:', min_age, ', oldest member is:', max_age)
    print('\nsort by len(name)', sort_m(members))
    print('\n')
    for i in range(1, 101, 10):
        print('dec', i, 'rome', solution(i))
