def decimal_to_roman(num: int):
    assert 0 < num < 5000 and int(num) == num, 'Number must be an integer in [1:4999]'
    clue = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
            90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ''
    for decimal, roman in sorted(clue.items(), reverse=True):
        while num >= decimal:
            result += roman
            num -= decimal
    print(result)
    return result


if __name__ == '__main__':
    print(decimal_to_roman(6))
    print(decimal_to_roman(14))
