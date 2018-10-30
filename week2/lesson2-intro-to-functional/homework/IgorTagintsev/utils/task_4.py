from re import search

def name_filter(data: list):
    return list(filter(lambda x: 'o' in x['name'], data))