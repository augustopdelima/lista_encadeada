class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def mesclagem(lista_a: No, lista_b: No):

    if lista_a is None:
        return lista_b

    if lista_b is None:
        return lista_a

    if lista_a.valor <= lista_b.valor:
        lista_a.proximo = mesclagem(lista_a.proximo, lista_b)
        return lista_a

    lista_b.proximo = mesclagem(lista_a, lista_b.proximo)
    return lista_b


def imprimir_lista(lista: No):

    valores = []
    cabeca_atual = lista

    while cabeca_atual is not None:
        valores.append(cabeca_atual.valor)
        cabeca_atual = cabeca_atual.proximo

    print(valores)


def criar_lista_encadeada(lista):

    if not lista:
        return None

    cabeca = No(lista[0])
    cabeca.proximo = criar_lista_encadeada(lista[1:])

    return cabeca


lista_a = criar_lista_encadeada([1, 3, 4, 7])
lista_b = criar_lista_encadeada([1, 2, 4, 5])


resultado = mesclagem(lista_a, lista_b)
imprimir_lista(resultado)
