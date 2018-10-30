def decimal_to_roman_num(n: int):
    dec_rom_list = [
        {'dec': 1, 'rom': 'I'},
        {'dec': 4, 'rom': 'IV'},
        {'dec': 5, 'rom': 'V'},
        {'dec': 9, 'rom': 'IX'},
        {'dec': 10, 'rom': 'X'},
        {'dec': 40, 'rom': 'XL'},
        {'dec': 50, 'rom': 'L'},
        {'dec': 90, 'rom': 'XC'},
        {'dec': 100, 'rom': 'C'},
        {'dec': 400, 'rom': 'CD'},
        {'dec': 500, 'rom': 'D'},
        {'dec': 900, 'rom': 'CM'},
        {'dec': 1000, 'rom': 'M'},
    ]
    dec_list = []
    while n > 0:
        for i in range(len(dec_rom_list)):
            if dec_rom_list[i]['dec'] <= n < dec_rom_list[i + 1]['dec']:
                dec_list.append({'dec': dec_rom_list[i]['dec'], 'rom': dec_rom_list[i]['rom']})
                n -= dec_rom_list[i]['dec']
            elif 3999 >= n >= 1000:
                dec_list.append({'dec': 1000, 'rom': 'M'})
                n -= 1000

    rom_num = ''
    for i in range(len(dec_list)):
        rom_num += dec_list[i]['rom']
    return rom_num
