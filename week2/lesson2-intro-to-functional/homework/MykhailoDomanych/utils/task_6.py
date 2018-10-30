
def sort_lenth(members: list) -> list:
    return sorted(members, key=lambda x: (len(x['name']), x['age']))
