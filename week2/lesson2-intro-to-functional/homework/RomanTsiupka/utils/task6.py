arab_to_romanian = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}


def encode_arab(arab):

    value = []

    for a in [*arab_to_romanian][::-1]:
        floor_div = arab // a

        base_divider = (10 ** (len(str(arab)) - 1))
        predict_number = arab + base_divider

        if not floor_div and predict_number // a == 1:
            value += [arab_to_romanian[base_divider], arab_to_romanian[a]]
            return value

        value += floor_div * [arab_to_romanian[a]]
        arab -= floor_div * a

        if arab == 0:
            return value

    return value


def solution(n):
    romanian = ""
    arab_as_str = str(n)

    # Let's split each numbers to small pieces, like: 1889 = 1000 + 900 + 80 + 9
    for idx, digit in enumerate(arab_as_str):
        to_convert = int(digit) * 10 ** (len(arab_as_str) - idx - 1)
        romanian += str.join('', encode_arab(to_convert))

    return romanian
