def members_with_o(members_list: list):
    return list(filter(lambda member_item: 'o' in member_item['name'].lower(), members_list))
