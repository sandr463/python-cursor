def dic_value_upper_case(members: list) -> list:
    return list(map(lambda v: {'age': v['age'], 'name': v['name'].upper()}, members))

