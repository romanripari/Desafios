COLUMNS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def column_number(name: str) -> int:
    if len(name) == 1:
        return COLUMNS.index(name) +1
    else:
        recursion = column_number(name[1:])
        
    return recursion + (COLUMNS.index(name[0])+1)  * len(COLUMNS) ** (len(name)-1)
    

print("Example:")
print(column_number("AA"))

assert column_number("XFD") == 16384
assert column_number("A") == 1
assert column_number("Z") == 26
assert column_number("AB") == 28
assert column_number("ZY") == 701
assert column_number('FXSHRXW') == 2147483647

print("The first mission is done! Click 'Check' to earn cool rewards!")
