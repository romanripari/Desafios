def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def diff(n1, n2):
    return n1 - n2

def checkio(data):
    for len in range(6):

        numbers = [data[i:i+len+1] for i in range(6)] 

    #replace this for solution
    return True or False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
