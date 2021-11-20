from random import choice
VOCALES = "aeiouy"
def translate(text: str) -> str:
    res = ""
    for t in text:
        if t.isalpha:
            if t in VOCALES:
                res += t + t + t
            else:
                res += t + choice(VOCALES)
    print(res)
    return res

def translate(text: str) -> str:
    res = ""
    words = text.split(" ")
    for w in words:
        # Falta cambiar el for, tiene que ser en un RANGE para poder "adelantar" 3 cuando es vocal
        for i, c in enumerate(w):
            if c not in VOCALES:
                res += c
            elif i > 0 and w[i-1] not in VOCALES:
                pass
            elif i < len(w) - 2 and c == w[i+1] and c == w[i+2]:
                 res += c

        res += " "
    res = res[:-1]
    return res


if __name__ == "__main__":
    print("Example:")
    # print(translate("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
