def sort_list(lst: list) -> list:
    return sorted(lst, key=lambda x: (len(x['name']), x['age']))
