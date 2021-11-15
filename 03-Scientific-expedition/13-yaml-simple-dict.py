def yaml(a):
    lista = a.split("\n")
    mydict = {}
    for l in lista:
        if l != "":
            k_val = l.split(":")
            val = k_val[1][1:].replace("\\", "")
            
            if val == "" or val.lower() == 'null':
                val = None 
            elif "null" in val.lower():
                val = "null"
            elif val[0]  == '"' and val[-1] == '"':
                val = val[1:-1]
            elif val.isnumeric():
                val = int(val)
            elif val.lower() == "false":
                val = False
            elif val.lower() == "true":
                val = True
            mydict[k_val[0]] = val

    return mydict


if __name__ == '__main__':
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
     'age: 12\n'
     '\n'
     'class: 12b') == {'age': 12,
     'class': '12b',
     'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'alive: false') == {'alive': False,
     'children': 6,
     'name': 'Bob Dylan'}
    print(1)
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding:') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    print(2)
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: null') == {'children': 6,
     'coding': None,
     'name': 'Bob Dylan'}
    print(3)
    assert yaml('name: "Bob Dylan"\n'
     'children: 6\n'
     'coding: "null" ') == {'children': 6,
     'coding': 'null',
     'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")

# if __name__ == '__main__':
#     print("Example:")
#     print(yaml("""name: Alex
# age: 12"""))

#     # These "asserts" are used for self-checking and not for an auto-testing
#     assert yaml("""name: Alex
# age: 12""") == {'age': 12, 'name': 'Alex'}
#     assert yaml("""name: Alex Fox
# age: 12

# class: 12b""") == {'age': 12,
#  'class': '12b',
#  'name': 'Alex Fox'}
#     print("Coding complete? Click 'Check' to earn cool rewards!")
