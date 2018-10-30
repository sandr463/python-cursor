def sum_max_min_members(members_list: list):
    sum_age = sum(list(map(lambda member_item: list(member_item.values())[0], members_list)))
    min_age = min(members_list, key=(lambda member_item: member_item['age']))
    max_age = max(members_list, key=(lambda member_item: member_item['age']))
    return sum_age, min_age, max_age
