from utils.task_1 import members as mb
from utils.task_2 import name_uppercase
from utils.task_3 import func_task3
from utils.task_4 import filter_data
from utils.task_5 import func_task5
from utils.task_6 import sorted_by_names
from utils.task_7 import convert_number
import copy

# Task 2

members = copy.deepcopy(mb)
print(f"Task 2\n\n {name_uppercase(members)}")
print("\n")

# Task 3

members = copy.deepcopy(mb)
print(f"Task 3\n\n {func_task3(members)}")
print("\n")

# Task 4

members = copy.deepcopy(mb)
print(f"Task 4 \n\n {filter_data(members)}")
print("\n")

# Task 5

members = copy.deepcopy(mb)
print(f"Task 5\n\n {func_task5(members)}")
print("\n")

# Task 6

members = copy.deepcopy(mb)
print(f"Task 6\n\n {sorted_by_names(members)}")
print("\n")

# Task 7 Advaced

print(f"Task 7\n\n {convert_number(2018)}")