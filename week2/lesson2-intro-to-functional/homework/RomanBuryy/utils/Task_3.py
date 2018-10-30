def percentage_of_progress(members: list):
    members = list(filter(lambda x: x["age"] < 200, members))
    return list(map(lambda x: {'age': x['age'], 'name': x['name'], 'load': x["age"] * 0.5}, members))
