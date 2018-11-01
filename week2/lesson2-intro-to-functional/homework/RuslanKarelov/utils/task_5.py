def func_task5(data: list):
    age_sum = sum(dic['age'] for dic in data)
    youngest_memb = (min(data, key=lambda x: x['age']))
    oldest_memb = (max(data, key=lambda x: x['age']))
    return age_sum, youngest_memb, oldest_memb
