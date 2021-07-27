"""Execicios em python
func range(start, stop, step)
print(list(range(3,27,2)
resultado = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]

tem inicio em 3
com intervalo de 2 em 2 até (n-2)
"""

# print(list(range(3, 27, 2)))
def conta_impar(n):
    return len(range(1, n, 2))


print(conta_impar(15))
