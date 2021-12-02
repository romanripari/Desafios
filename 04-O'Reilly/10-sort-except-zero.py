from typing import Iterable

# Bubble sort with an exception
def except_zero(items: list) -> Iterable:
    for i, _ in enumerate(items):
        for j in range(0,i):
            if items[i] != 0 and items[i] < items[j]:
                items[j], items[i] = items[i], items[j] 
    return items
