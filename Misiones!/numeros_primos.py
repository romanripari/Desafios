
from enum import unique


def primo(maximo):
    lista_no_primos = []

    for m in range(2,len(maximo)+1):
        for multi in range(m,max(maximo)+1):
            if multi % m ==0:
                if multi not in lista_no_primos:
                    lista_no_primos.append(multi)
    lista_no_primos.sort()
    print(lista_no_primos)


def run():
    maximo = range(1,15)
    primo(maximo)    

if __name__ == '__main__':
    run()