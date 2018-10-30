def filter_o_name(members_list: list):
    # return [member for member in members_list if 'o' in member['name'].lower()]       # var 1
    return list(filter(lambda member: 'o' in member['name'].lower(), members_list))  # var 2


if __name__ == '__main__':
    import copy
    from utils.task_1 import members as MEMBERS

    members = copy.deepcopy(MEMBERS)

    print(members)
    print(filter_o_name(members))
