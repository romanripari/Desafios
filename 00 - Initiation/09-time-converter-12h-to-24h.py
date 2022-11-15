from datetime import datetime, timedelta
def time_converter(time):
    horas = int(time[:time.find(":")])
    minutos = int(time[time.find(":")+1:time.find(" ")])
    if "p" in time:
        horas += 12
    elif horas == 12:
        horas = 0
    if horas == 24: horas = 12
    time = f'{horas:02d}:{minutos:02d}'
    return time

# Code from @a.kapral26
import time
def time_converter(tim):
    tim = tim.replace(' ','').replace('.', '')
    times = time.strptime(tim.upper(), '%I:%M%p')
    return time.strftime('%H:%M', times)


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 a.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
