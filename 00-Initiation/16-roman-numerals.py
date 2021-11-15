def checkio(n):
    # roman = []
    # rules = [["M", 1000],["D", 500],["C", 100],
    #         ["L", 50],["X", 10],
    #         ["V", 5],["I", 1]]
    # for r in rules:
    #     while data >= r[1]:
    #         roman.append(r[0])
    #         data -= r[1] 
    # roman = "".join(roman)
    # rules_2 = [["DCCCC", "CM"], ["CCCC", "CD"],
    #         ["LXXXX", "XC"], ["XXXX", "XL"],
    #         ["VIIII", "IX"], ["IIII", "IV"]]
    # for r in rules_2:
    #     roman = roman.replace(r[0], r[1])
    # return roman
    result = ''
    for arabic, roman in zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
                             'M     CM   D    CD   C    XC  L   XL  X   IX V  IV I'.split()):
        result += n // arabic * roman
        n %= arabic
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '4199'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')