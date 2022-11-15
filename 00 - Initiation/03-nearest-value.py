def nearest_value(values: set, one: int) -> int:
    res = max(values)
    distance = abs(res-one)
    for v in values:
        if (abs(v-one) < distance) or ( abs(v-one) == distance and v < res):
            res = v
            distance = abs(v-one)
            
    return res


if __name__ == '__main__':
    print("Example:")
    # print(nearest_value({4, 7, 10, 11, 12, 17}, 9))
    print(nearest_value([0,-2],-1))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
