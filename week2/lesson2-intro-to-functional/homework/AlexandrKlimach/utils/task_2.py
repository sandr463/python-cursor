def load_progress(lst: list) -> list:
    for dct in lst:
        dct['load'] = 100 * dct['age'] / 200
    return list(filter(lambda x: x['age'] < 200, lst))
