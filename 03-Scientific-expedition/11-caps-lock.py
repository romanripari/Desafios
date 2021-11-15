def caps_lock(text: str) -> str:
    texto  = ""
    all_caps = False
    for t in text:
        if t == "a":
            all_caps = not all_caps
        elif all_caps:
            texto += t.upper()
        else:
            texto += t

    return texto


if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")
