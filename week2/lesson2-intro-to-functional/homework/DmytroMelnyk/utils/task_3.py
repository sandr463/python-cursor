def filter_and_load(l: list):
    """
    Each member will be exclude of group after reaching the age of 200 years.
    Add field "load" for each member, which shows percentage of progress
    :param l: input list of dict
    :return: changed list
    """
    l = list(filter((lambda x: x['age'] < 200), l))
    list(map(lambda x: x.update({'load': (x['age']) / 2}), l))
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
    print(filter_and_load(members))
