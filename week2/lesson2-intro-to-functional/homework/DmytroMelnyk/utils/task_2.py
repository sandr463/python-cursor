def uppercase_list(l: list):
    """
    For each member make his name uppercase
    :param l: input list of dict
    :return: changed list l
    """
    list(map(lambda x: x.update({'name': x['name'].upper()}), l))
    return l


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

    print(members)
    print(uppercase_list(members))
