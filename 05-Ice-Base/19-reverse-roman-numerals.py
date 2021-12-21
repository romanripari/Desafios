def reverse_roman(roman_string):
    rules = (("DCCCC", "CM"), ("CCCC", "CD"),
            ("LXXXX", "XC"), ("XXXX", "XL"),
            ("VIIII", "IX"), ("IIII", "IV"))
    for r in rules:
        roman_string = roman_string.replace(r[1], r[0])

    numbers = (("M", 1000),("D", 500),("C", 100),("L", 50),("X", 10),("V", 5),("I", 1))

    return sum([n[1] * roman_string.count(n[0]) for n in numbers])


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
    print('Great! It is time to Check your code!');