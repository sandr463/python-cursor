def sorted_by_names(data: list):
    data = sorted(data, key=lambda x: (len(x['name']), x['age']))
    return data
