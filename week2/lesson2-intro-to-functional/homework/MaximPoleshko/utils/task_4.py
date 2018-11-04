def left_members(memb: list) -> list:
    without_o = []
    for m in memb:
        if not 'o' in m['name'].lower():
            without_o.append(m)
    return without_o