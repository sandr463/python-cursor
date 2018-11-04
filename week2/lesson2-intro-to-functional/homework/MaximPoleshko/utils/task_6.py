def sort_m(memb: list) -> list:
    return sorted(memb, key=lambda x: (len(x['name']), x['age']))