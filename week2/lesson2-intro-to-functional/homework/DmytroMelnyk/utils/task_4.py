def filter_o_left(l: list):
    """
    Left only those members who have letter 'o' in names.
    :param l: input list of dict
    :return: filtered list
    """
    return list(filter(lambda x: 'o' in x['name'], l))


if __name__ == '__main__':
    members = [
        {'age': 43, 'name': 'Denis'},
        {'age': 49, 'name': 'Roman'},
        {'age': 36, 'name': 'Godzilla'},
        {'age': 47, 'name': 'Spike'},
        {'age': 31, 'name': 'SuperMan'},
        {'age': 49, 'name': 'Batman'},
        {'age': 37, 'name': 'Claus'},
        {'age': 55, 'name': 'Frank'},
        {'age': 83, 'name': 'Homer'}
    ]

    print(filter_o_left(members))
