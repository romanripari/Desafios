def goes_after(word: str, first: str, second: str) -> bool:
    if len(word) > 1:
        for i in range(len(word)-1):
            if word[i] == first:
                return word[i+1] == second
            if word[i] == second:
                return False
    return False

if __name__ == '__main__':
    print("Example:")
    print(goes_after("almaz","m","a"))
    print(goes_after('world', 'w', 'o'))
    goes_after("almaz","m","a")
    # These "asserts" are used for self-checking and not for an auto-testing
    assert goes_after('world', 'w', 'o') == True
    assert goes_after('world', 'w', 'r') == False
    assert goes_after('world', 'l', 'o') == False
    assert goes_after('panorama', 'a', 'n') == True
    assert goes_after('list', 'l', 'o') == False
    assert goes_after('', 'l', 'o') == False
    assert goes_after('list', 'l', 'l') == False
    assert goes_after('world', 'd', 'w') == False
    assert goes_after('world', 'l', 'd') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
