def ages(memb_list):
    summ_age = sum(map(lambda x: x['age'], memb_list))
    min_age = min(memb_list, key = lambda x: x['age'])
    max_age = max(memb_list, key = lambda x: x['age'])
    return summ_age, min_age, max_age