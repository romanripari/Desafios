def checkio(number: int) -> int:
    if number == 0:
        return 1
    elif number / 10 < 1:
        return number
    else:
        aux = number % 10 if number % 10 != 0 else 1
        
    return  aux * checkio(int((number-number % 10)/10))



if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))
    
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
