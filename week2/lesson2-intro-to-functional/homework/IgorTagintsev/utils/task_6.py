def sort_members_by_name_length(list_of_members: list):
    return sorted(list_of_members, key=lambda x: (len(x['name']), x['age']))

