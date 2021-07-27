"""
Exercicios com strings

"""
print("*"*40)
print("")
print("BRINCANDO COM STRING USANDO PALINDROMO")
print("")
print("*"*40)
enter = input("Digite uma palavra ou frase: ")


def palindromo(enter):
    if enter[::-1] == enter:
        return f"A palavra {enter} é um palindromo"
    else:
        return f"A palavra {enter} não é um palindromo"


print(palindromo(enter))
