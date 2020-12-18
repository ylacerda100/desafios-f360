file = open("textoB.txt", "r")

alfabeto = 'kbwrqdnfxjmlvhtcgzps'

# função para eliminar palavras repetidas do texto B


def get_palavras_sem_repeticao():
    lista_unicos = []
    with file as arquivo:
        for linha in arquivo:
            palavras = linha.split()
            for palavra in palavras:
                if palavra not in lista_unicos:
                    lista_unicos.append(palavra)
    file.close()
    return lista_unicos
