def add_load(memb: list) -> list:
    for m in memb:
      m['load'] = m['age'] / 200 * 100
    return memb