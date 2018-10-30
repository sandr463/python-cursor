def filter_dict(members: list):
    return list(filter(lambda x: "o" in x["name"], members))
