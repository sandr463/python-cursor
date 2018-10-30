def name_uppercase(lst: list) -> list:
    for dct in lst:
        dct['name'] = dct['name'].upper()
    return lst
