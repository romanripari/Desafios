from typing import Union


def sun_angle(time: str) -> Union[int, str]:
    h = int(time[:2])
    m = int(time[3:]) 
    if h < 6 or (h > 17 and m > 0):
        return "I don't see the sun!"
    angulo = (h-6) / 12 * 180 + (m) / 60 * (180/12)

    return angulo


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
