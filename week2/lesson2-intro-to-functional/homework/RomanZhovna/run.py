from utils.task2 import upmembers
from utils.task3 import filtered_list
from utils.task4 import with_o
from utils.task5 import print_values
from utils.task6 import sort_list
from utils.task7 import arabic2roman

members = [
  {'age': 43, 'name': 'Denis'},
  {'age': 49, 'name': 'Roman'},
  {'age': 36, 'name': 'Godzilla'},
  {'age': 47, 'name': 'Spike'},
  {'age': 31, 'name': 'SuperMan'},
  {'age': 230, 'name': 'Batman'},
  {'age': 37, 'name': 'Claus'},
  {'age': 55, 'name': 'Frank'},
  {'age': 83, 'name': 'Homer'}
]

if __name__ == "__main__":
    print(upmembers(members))
    print(filtered_list(members))
    print(with_o(members))
    print(print_values(members))
    print(sort_list(members))
    print(arabic2roman(2789))
