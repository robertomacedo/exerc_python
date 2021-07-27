"""
Ercecicios com strings

"""


def palindromo(s):
    if s[::-1] == s:
        return True
    else:
        return False


print(palindromo("asa"))
