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
    for w in text.split(" "):
        i = 0        
        while i < len(w):
            if w[i] not in VOCALES:
                res += w[i]
                i += 1
            elif i < len(w) - 2 and w[i] == w[i+1] and w[i] == w[i+2]:
                 res += w[i]
                 i += 2
            i += 1

        res += " "

    return res[:-1]


if __name__ == "__main__":
    print("Example:")
    # print(translate("hello"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert translate("hieeelalaooo") == "hello"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
    assert translate("aaa bo cy da eee fe") == "a b c d e f"
    assert translate("sooooso aaaaaaaaa") == "sos aaa"
    print("Coding complete? Click 'Check' to earn cool rewards!")
