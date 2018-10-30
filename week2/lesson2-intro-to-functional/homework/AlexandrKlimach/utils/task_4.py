def return_values(lst: list) -> tuple:
    sum_age = sum(dct['age'] for dct in lst)
    youngest_member = min(lst, key=lambda x: x['age'])
    oldest_member = max(lst, key=lambda x: x['age'])
    return sum_age, youngest_member, oldest_member
