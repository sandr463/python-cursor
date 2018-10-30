def sort_members(member_list: list):
    return sorted(member_list, key=lambda member_item: (len(member_item['name']), member_item['age']))
