from functools import reduce


def age_statistic(members_list: list):
    age_sum = reduce(lambda x, y: x + y, [member['age'] for member in members_list])
    oldest = reduce(lambda x, y: x if x['age'] > y['age'] else y, members_list)
    youngest = reduce(lambda x, y: x if x['age'] < y['age'] else y, members_list)
    return age_sum, oldest, youngest


if __name__ == '__main__':
    import copy
    from utils.task_1 import members as MEMBERS

    members = copy.deepcopy(MEMBERS)

    print(members)
    print(age_statistic(members))
