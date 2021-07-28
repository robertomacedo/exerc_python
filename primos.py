


enter = int(input("Digite um valor: "))


def primo(enter):
    for p in range(2, enter):
        if enter % p == 0:
            return f"{enter} não eh primo"
        else:
            return f"{enter} eh primo"


print(primo(enter))
