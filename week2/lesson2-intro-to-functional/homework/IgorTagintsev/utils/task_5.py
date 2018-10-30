from functools import reduce

def age(data: list):
    summ = reduce(lambda x, y: x + y, [member['age'] for member in data])
    young = min(data, key=lambda x: x['age'])
    old = max(data, key=lambda x: x['age'])
    return summ, young, old
