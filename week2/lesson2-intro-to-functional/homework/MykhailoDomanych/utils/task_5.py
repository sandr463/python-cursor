def sum_max_min_age (members: list) -> list:
    result = []
    result.append(sum(dct['age'] for dct in members))
    result.append(min(members, key=lambda x: x['age']))
    result.append(max(members, key=lambda x: x['age']))
    return result
