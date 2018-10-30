import copy


def filtered_list(l: list) -> list:
    def addload(d: dict)-> dict:
        d['load'] = d['age']*100/200
        return d
    return list(map(addload, list(filter(lambda x: x['age'] < 200, copy.deepcopy(l)))))
