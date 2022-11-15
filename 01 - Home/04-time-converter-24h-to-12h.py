def time_converter(time):
    h = int(time[:2])
    if h > 12:
        h -=12
        ampm = "p.m."
    elif h == 12:
        ampm = "p.m."
    elif h == 0:
        h = 12
        ampm = "a.m."
    else:
        ampm = "a.m."
    return f'{h}:{time[3:]} {ampm}'

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
