def checkio(line1: str, line2: str) -> str:
    words = ",".join(sorted([w for w in line1.split(",") if w in line2.split(",")]))

    return words


if __name__ == '__main__':
    print("Example:")
    print(checkio("mega,cloud,two,website,final","window,penguin,literature,network,fun,cloud,final,sausage"))
    print(checkio('hello,world', 'hello,earth'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio('hello,world', 'hello,earth') == 'hello'
    assert checkio('one,two,three', 'four,five,six') == ''
    assert checkio('one,two,three','four,five,one,two,six,three') == 'one,three,two'
    print("Coding complete? Click 'Check' to earn cool rewards!")
