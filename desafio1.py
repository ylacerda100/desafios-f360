file = open("textoB.txt", "r")

letras_foo = ["s", "l", "f", "w", "k"]

with file as arquivo:
    count = 0
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            if len(palavra) == 3 and palavra[-1:] not in letras_foo and "d" not in palavra:
                count += 1

print(count)
