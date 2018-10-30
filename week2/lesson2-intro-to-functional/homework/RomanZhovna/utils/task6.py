def sort_list(l: list) -> list:
    return sorted(l, key=lambda x: (len(x['name']), x['age']))
