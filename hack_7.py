"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    indice = 5

    while indice >= 0:
        result.append(indice)
        indice -= 1
    return result