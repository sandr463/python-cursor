def sort_m(mem: list):
    mem = sorted(mem, key=lambda i: (len(i['name']), i['age']))
    return mem
