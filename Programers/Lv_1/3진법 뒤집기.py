"""
def deci_to_thir(a):
    thir=''
    while True:
        d, m = divmod(a, 3)
        thir = str(m) + thir
        if d > 2:
            a = d
        elif d > 0:
            thir = str(d) + thir
            break
    return thir
"""
def numeral_system(number, base):
    NOTATION = '012'
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base)+n if q else n

def thir_to_deci(a):
    deci = 0
    for idx, i in enumerate(a):
        deci += (3**idx)*int(i)
    return deci
    
def solution(n):
    return thir_to_deci(numeral_system(n, 3))