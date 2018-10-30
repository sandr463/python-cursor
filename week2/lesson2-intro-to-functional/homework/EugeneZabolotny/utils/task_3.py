def age_loader(members_list: list):
    for member in members_list:
        load = member['age'] * 100 / 200
        member['load'] = int(load) if load.is_integer() else load


if __name__ == '__main__':
    import copy
    from utils.task_1 import members as MEMBERS

    members = copy.deepcopy(MEMBERS)

    print(members)
    age_loader(members)
    print(members)
