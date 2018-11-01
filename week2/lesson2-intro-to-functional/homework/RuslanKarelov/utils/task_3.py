def func_task3(data: list):
    data = list(filter(lambda x: x['age'] < 200, data))
    for i in data:
        i['load'] = i['age'] * 100 / 200
    return data
