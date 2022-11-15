def i_love_python():
    who = "I"
    verb = "love"
    noun = "Python"
    exclamation = "!"
    try:
        text = f'{who} {verb} {noun}{exclamation}'
    except ValueError:
        raise "I love Python!"

    return text

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
