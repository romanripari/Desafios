def yaml(a):
    lista = a.split("\n")
    mydict = {}
    for l in lista:
        if l != "":
            keys = l.split(":")
            valor = keys[1][1:]
            try:
                valor = int(valor)
            except:
                valor = valor
            mydict[keys[0]] = valor

    return mydict


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
