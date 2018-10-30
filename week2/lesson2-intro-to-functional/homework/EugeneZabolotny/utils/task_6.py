def sort_by_name_length(members_list: list):
    members_list.sort(key=lambda member: member['age'])
    return sorted(members_list, key=lambda member: len(member['name']))


if __name__ == '__main__':
    import copy
    from utils.task_1 import members as MEMBERS

    members = copy.deepcopy(MEMBERS)

    print(members)
    print(sort_by_name_length(members))
