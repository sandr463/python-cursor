# creating new list using list and dict comprehension
def upmembers(l: list) -> list:
    return [{k: (v.upper() if k == 'name' else v) for (k, v) in d.items()} for d in l]
