def only_o(members: list) -> list:
    return list(filter(lambda x: "o" in x["name"], members))
