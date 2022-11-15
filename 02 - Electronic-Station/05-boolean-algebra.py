OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")


# boolean=lambda x,y,o:1&~"dimpleqonx".index(o[1])>>y>>x>>y
def boolean(x, y, operation):
    if operation == "conjunction":
        return x == y and x == 1
    if operation == "disjunction":
        return x == 1 or y == 1
    if operation == "implication":
        return x == 0 or (x == 1 and y == 1)
    if operation == "exclusive":
        return x != y
    if operation == "equivalence":
        return x == y 

boolean = lambda x, y, o: {'co':x and y,'di':x or y,'im':y if x else 1,'ex':x!=y,'eq':x==y}[o[:2]]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
    print('All good! Go and check the mission.')
