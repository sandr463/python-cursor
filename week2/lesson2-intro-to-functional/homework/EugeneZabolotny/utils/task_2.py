def name_to_upper(members_list: list):
    for member in members_list:
        member['name'] = member['name'].upper()


if __name__ == '__main__':
    import copy
    from utils.task_1 import members as MEMBERS

    members = copy.deepcopy(MEMBERS)

    print(members)
    name_to_upper(members)
    print(members)
