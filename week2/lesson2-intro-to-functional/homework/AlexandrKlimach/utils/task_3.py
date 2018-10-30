def find_letter(lst: list) -> list:
    return list(filter(lambda x: 'o' in x['name'].lower(), lst))
