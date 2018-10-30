def load_progress(members: list) -> list:
    list(map(lambda x: x.update({'load': (x['age']) * 0.5}), members))
    return list(filter((lambda x: x['age'] < 200), members))


