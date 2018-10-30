def load_func(members_list: list):
    list(map(lambda member_item: {'age': member_item['age'], 'name': member_item['name'], 'load': member_item['age']/2},
         members_list))
    return list(filter(lambda member_item: member_item['age'] < 200, members_list))
