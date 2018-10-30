from functools import reduce


def print_values(l: list) -> list:
    summary = [reduce(lambda x, y: x+y, list(map(lambda x: x['age'], l)))]
    min_age = list(filter(lambda x: x['age'] == min(list(map(lambda x: x['age'], l))), l))
    max_age = list(filter(lambda x: x['age'] == max(list(map(lambda x: x['age'], l))), l))
    return summary + min_age + max_age
