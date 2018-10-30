def makeSort(p_list: list) -> list:
    return sorted(p_list, key=lambda k: (len(k['name']), k['age']))
