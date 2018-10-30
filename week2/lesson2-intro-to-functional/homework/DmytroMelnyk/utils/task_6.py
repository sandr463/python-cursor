def sort_len_name(l: list):
    """
    Sort members by length of their names. If length of names is equal than sort by age.
    :param l: input list of dict
    :return: sorted list
    """

    return sorted(l, key=lambda x: (len(x['name']), (x['age'])))


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

    print(sort_len_name(members))