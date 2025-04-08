"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    lista = [1, 2, 3]
    result = []
    i = 0
    while i < len(lista):
        result.append(lista[i])
        result.append('@')
        i += 1
    return result
print(fn_hack_9())