# this is "simple" convertor for arabic to roman conversion and numbers from initial_map are enough only for arabic numbers up to 3999.
def arabic2roman(input_number: int) -> str:
    assert 0 < input_number <= 3999 and int(input_number)
    initial_map = [(1000, "M"),
                   (900, "CM"),
                   (500, "D"),
                   (400, "CD"),
                   (100, "C"),
                   (90, "XC"),
                   (50, "L"),
                   (40, "XL"),
                   (10, "X"),
                   (9, "IX"),
                   (5, "V"),
                   (4, "IV"),
                   (1, "I")]
    result = ''
    while input_number > 0:
        for numeric, roman in initial_map:
            while input_number >= numeric:
                result += roman
                input_number -= numeric
    return result
