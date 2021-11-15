from datetime import datetime
def days_diff(a, b):
    date_a = datetime(year = a[0], month = a[1], day = a[2])
    date_b = datetime(year = b[0], month = b[1], day = b[2])
    diff = date_b - date_a
    return abs(diff.days)

if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
