from utils.task_2 import up_name
from utils.task_3 import add_load
from utils.task_4 import left_members
from utils.task_5 import ages
from utils.task_6 import sort_m

members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 49, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'},
]

print(up_name(members))
print(add_load(members))
print(left_members(members))
print(ages(members))
print(sort_m(members))
