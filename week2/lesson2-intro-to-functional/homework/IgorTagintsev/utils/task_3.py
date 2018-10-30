def load(l: list):
    list(map(lambda x: x.update({'load': (x['age'])/2}), l))
    return list(filter((lambda x: x['age'] < 200), l))

