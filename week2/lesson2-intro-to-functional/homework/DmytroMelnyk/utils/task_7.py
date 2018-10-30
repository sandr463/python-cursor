def convert_dec_roman(inp):
    """
    Function that will convert decimal values to Roman Numerals
    :param inp: arabian num
    :return: Roman num
    """
    for k, v in to_roman.items():
        if inp == k:
            return v
        if inp > k:
            temp = v
            temp1 = k

    remain = inp - temp1
    return temp + convert_dec_roman(remain)


if __name__ == '__main__':
    to_roman = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X', 20: 'XX',
                30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX',
                90: 'XC', 100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D',
                600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1000: 'M',
                2000: 'MM', 3000: 'MMM'}

    print(convert_dec_roman(78))
