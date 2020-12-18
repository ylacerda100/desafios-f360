file = open("textoB.txt", "r")

alfabeto_kinglon = ['k', 'b', 'w', 'r', 'q', 'd', 'n', 'f',
                    'x', 'j', 'm', 'l', 'v', 'h', 't', 'c', 'g', 'z', 'p', 's']

numeros_bonitos = 0

with file as arquivo:
    for linha in arquivo:
        palavras = linha.split()
        for palavra in palavras:
            n = 0
            p = 1
            for letra in palavra:
                n += alfabeto_kinglon.index(letra) * p
                p *= 20
            if n >= 440566 and n % 3 == 0:
                numeros_bonitos += 1
file.close()
print(numeros_bonitos)
