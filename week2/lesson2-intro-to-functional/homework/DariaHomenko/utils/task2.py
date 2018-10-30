def name_uppercase(member_list: list):
    return list(map(lambda member_item: {'age': member_item['age'], 'name': member_item['name'].upper()}, member_list))
