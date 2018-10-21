from task_1 import members

def three_values_func(members:list):
    age_list_members = sum([i['age'] for i in members])
    age_list_members_min = min(members, key=lambda x: x['age'])
    age_list_members_max = max(members, key=lambda x: x['age'])
    return age_list_members, age_list_members_min, age_list_members_max

print(three_values_func(members))