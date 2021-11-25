def checkio(number):
    i = 0
    n = 0
    while n < number:
        i += 1
        n += i 
    res = i-1 if n > number else i 
    print(res)
    return res

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1) == 1, "1st example"
    assert checkio(2) == 1, "2nd example"
    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"


    # A = Π x r²