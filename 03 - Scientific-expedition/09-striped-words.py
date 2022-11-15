import re

def isvowel(_):
    return _.lower() in "aeiouy"

def checkio(line: str) -> str:
    words = re.split(r'(\W+)', line, flags=re.IGNORECASE)
    res = []
    for word in words:
        is_ok = True
        for i, w in enumerate(word):
            if i < len(word)-1:
                if w.isnumeric() or isvowel(w) == isvowel(word[i+1]):
                    is_ok = False
        if is_ok and len(word) > 1:
            res.append(w)

    return len(res)


if __name__ == '__main__':
    print("Example:")
    print(checkio('My name is ...'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert checkio("1st 2a ab3er root rate") == 1
    assert checkio('My name is ...') == 3
    assert checkio('Hello world') == 0
    assert checkio('A quantity of striped words.') == 1
    assert checkio('Dog,cat,mouse,bird.Human.') == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")
