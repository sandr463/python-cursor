def convert_number(arabic_number: int):
    roman_numb = {1: 'I',4: 'IV', 5: 'V', 9: 'XI', 10: 'X',
              40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 
              400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    your_num = ""
    i = arabic_number
    while  i > 0:
        key = max([x for x in roman_numb.keys() if x <= i])  
        your_num = your_num + roman_numb[key]
        i = i - key
    return your_num
print(convert_number(78))