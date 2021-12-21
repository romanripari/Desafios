# %%
import itertools
from pprint import pprint
def suma(n, i):     
    return n + i
def resta(n, r):    
    return n - r
def divide(n, d):  
    return n / d

def multi(n, m):    
    return n * m
def potencia(n, p): 
    return n ** p
def signo(n):       
    return - n
def quita(n):
    if n > 0:
        if len(str(n)) > 1:
            return float(str(n)[:-1])
        else:
            return 0
    elif n == 0:
        return 0
    else:
        n = -n
        if len(str(n)) > 1:
            return - float(str(n)[:-1])
        else:
            return 0

def agrega(n, s):
    if n == int(n):
        return float(str(int(n)) + str(s))
    return float(str(n) + str(s))

def gira(n):
    if n > 0:
        if n == int(n):
            return float( str(int(n))[::-1] )
        return float( str(n)[::-1] )
    elif n == 0:
        return 0
    else:
        n = -n
        if n == int(n):
            return - float( str(int(n))[::-1] )
        return  - float( str(n)[::-1] )

def transforma(n, i, j):
    if n == int(n):
        res = int(str(int(n)).replace(str(i), str(j)))
    else:
        res = float(str(n).replace(str(i), str(j)))
    return res

def sumatoria(n):
    if n == int(n):
        sum = 0
        if n >= 0:
            for digit in str(n):  
                if digit != ".":    
                    sum += int(digit)        
            return sum
        else:
            for digit in str(n):  
                if digit != "." and digit != "-":    
                    sum += int(digit)        
            return - sum

    else:
        return n
    

def testea(test, combinaciones, gol):
    for combi in combinaciones:
        n = test
        numeros = []
        for Co in combi:
            C = Co[0]
            item = Co[1]
            if C == ">>":
                n = agrega(n, item)
            elif C == "*":
                n = multi(n, item)
            elif C == "g":
                n = gira(n)
            elif C == "+":
                n = suma(n,item)
            elif C == "/":
                n = divide(n,item)
            elif C == "-":
                n = resta(n,item)
            elif C == "+-":
                n = signo(n)
            elif C == "<<":
                n = quita(n)
            elif C == "++":
                n = sumatoria(n)
            elif C == "tr":
                n = transforma(n, item[0], item[1])
            numeros.append(n)
        if n == gol:
            return combi, numeros
    return "No se encontró", "No se encontró"

def run(): 
    n = 105
    movimientos = 5
    gol = -17
    botones = [
        ("-", 5),
        ("/", 5),
        ("*", 4),
        ("+-", 0),
        ("++", 0),

        # ("tr", (12, 21)),

         ] 


    combinaciones = [p for p in itertools.product(botones, repeat=movimientos)]

    resultado1, resultado2 = testea(n, combinaciones, gol)
    for i, r in enumerate(resultado1):
        print(r, "->", resultado2[i])

if __name__ == '__main__':
    run()