def total_value(tot: list):
    s_age = sum([x.get('age') for x in tot])
    mi_age = min(tot, key=lambda x: x.get('age'))
    ma_age = max(tot, key=lambda x: x.get('age'))
    return s_age, mi_age, ma_age
