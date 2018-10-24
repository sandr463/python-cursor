def arab_to_rom(number):
    if number < 0 or number > 4000:
        return "Number out of range"
    roman_arab_dict = [
        ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
        ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
        ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
    ]
    roman_numerals = ''
    for numeral, value in roman_arab_dict:
        while value <= number:
            number -= value
            roman_numerals += numeral
    return roman_numerals
