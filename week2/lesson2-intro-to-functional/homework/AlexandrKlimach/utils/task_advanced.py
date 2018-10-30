def int_to_rm(num: int) -> str:
    rm_table = {1000: 'M', 900: 'CM', 500: "D", 400: 'CD', 100: 'C', 90: 'XC',
                50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: "V", 4: 'IV', 1: 'I'}
    rm = ""
    for key in rm_table.keys():
        count = int(num / key)
        rm += rm_table[key] * count
        num -= key * count
    return rm
