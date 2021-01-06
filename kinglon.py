letras_foo = ["s", "l", "f", "w", "k"]

alfabeto_kinglon = ['k', 'b', 'w', 'r', 'q', 'd', 'n', 'f',
                    'x', 'j', 'm', 'l', 'v', 'h', 't', 'c', 'g', 'z', 'p', 's']


class Kinglon:

    def __init__(self, file):
        self.__file = file

    def encontrar_preposicoes(self):
        with open(self.__file, 'r') as arquivo:
            count = 0
            for linha in arquivo:
                palavras = linha.split()
                for palavra in palavras:
                    if len(palavra) == 3 and palavra[-1:] not in letras_foo and "d" not in palavra:
                        count += 1
            return count

    def encontrar_verbos(self):
        with open(self.__file, 'r') as arquivo:
            verbos = 0
            for linha in arquivo:
                palavras = linha.split()
                for palavra in palavras:
                    if len(palavra) >= 8 and palavra[-1:] in letras_foo:
                        verbos += 1
        return verbos

    def verbos_primeira_p(self):
        with open(self.__file, 'r') as arquivo:
            verbos = 0
            for linha in arquivo:
                palavras = linha.split()
                for palavra in palavras:
                    if len(palavra) >= 8 and palavra[-1:] in letras_foo and palavra[0] not in letras_foo:
                        verbos += 1
        return verbos

    def get_palavras_sem_repeticao(self):
        alfabeto = 'kbwrqdnfxjmlvhtcgzps'
        lista_unicos = []
        with open(self.__file, 'r') as arquivo:
            for linha in arquivo:
                palavras = linha.split()
                for palavra in palavras:
                    if palavra not in lista_unicos:
                        lista_unicos.append(palavra)
        return lista_unicos

    def numeros_bonitos(self):
        numeros_bonitos = 0
        with open(self.__file, 'r') as arquivo:
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
        return numeros_bonitos
