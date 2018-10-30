from functools import reduce


def summary(members: list):
    youngest = min(members, key=lambda x: x["age"])

    oldest = max(members, key=lambda x: x["age"])

    sum_age = reduce(lambda x, y: x + y, list(i["age"] for i in members))

    return sum_age, youngest, oldest
