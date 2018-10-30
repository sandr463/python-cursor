def upper_case(mem: list):
    for i in mem[:]:
        i['name'] = i['name'].upper()
        i['load'] = int(i['age'] / 2)
        if i['age'] >= 200: mem.remove(i)
    return mem
