"""
n ** (1/8) % 1 == 0 -> raiz oitava de n
n ** (1/4) % 1 == 0 -> raiz quarta de n
n ** (1/2) % 1 == 0 -> raiz quadrada de n

"""


def sqrt_perfect(n):
    if n ** (1/8) % 1 == 0:
        return True
    else:
        return False


print(sqrt_perfect(256))
