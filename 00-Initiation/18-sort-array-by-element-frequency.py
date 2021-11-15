def frequency_sort(items):
    import collections
    if len(set(items)) == len(items):
        times = items
    else:
        times = [n for n,count in collections.Counter(items).most_common() for i in range(count)]
    return times

if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([1,1,2,2]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")

