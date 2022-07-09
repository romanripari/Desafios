
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)

def run():
    a = 28
    b = 69
    el_mcd = mcd(a, b)
    print(el_mcd)

if __name__ == '__main__':
    run()