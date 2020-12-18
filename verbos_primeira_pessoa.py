file = open("textoB.txt", "r")

letras_foo = ["s", "l", "f", "w", "k"]

with file as arquivo:
    verbos = 0
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            # encontrando verbos kinglon primeira pessoa
            if len(palavra) >= 8 and palavra[-1:] in letras_foo and palavra[0] not in letras_foo:
                verbos += 1
print(verbos)
file.close()
