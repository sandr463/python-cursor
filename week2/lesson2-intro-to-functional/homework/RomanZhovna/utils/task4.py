def with_o(l: list) -> list:
    return list(filter(lambda x: 'o' in x['name'].lower(), l))
