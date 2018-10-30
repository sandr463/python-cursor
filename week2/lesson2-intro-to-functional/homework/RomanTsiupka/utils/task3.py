def left_o(mem: list):
    mem = list(filter(lambda mem: 'o' in mem['name'].lower(), mem))
    return mem
