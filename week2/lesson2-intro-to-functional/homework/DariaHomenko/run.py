from my_moduls import *

if __name__ == '__main__':
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

print('--------------Task 1--------------', end='\n\n')
print(members, end='\n\n')
print('--------------Task 2--------------', end='\n\n')
print(name_uppercase(members), end='\n\n')
print('--------------Task 3--------------', end='\n\n')
print(load_func(members), end='\n\n')
print('--------------Task 4--------------', end='\n\n')
print(members_with_o(members), end='\n\n')
print('--------------Task 5--------------', end='\n\n')
print(sum_max_min_members(members))
print('--------------Task 6--------------', end='\n\n')
print(sort_members(members), end='\n\n')
print('--------------Task 7--------------', end='\n\n')
print(decimal_to_roman_num(3999), end='\n\n')
