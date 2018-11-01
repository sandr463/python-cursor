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
def my_function(data:list):
    list_with_data = []
    list_with_data.append(sum(list(map(lambda x: x['age'], data))))
    list_with_data.append(min(data, key=lambda x: x['age']))
    list_with_data.append(max(data, key=lambda x: x['age']))
    return list_with_data
print(my_function(members))