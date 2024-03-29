def encontrar_tupla_por_valor(valor: int, array: list[tuple[int, int, int]]):
    tuplas: list[tuple[int, int]] = []

    for tupla in array:
        if valor == tupla[0]:
            tuplas.append(tupla)

    return tuplas

def encontrar_tupla_por_subtupla(valor: tuple[int, int], array: list[tuple[int, int, int]]):
    tuplas: list[tuple[int, int]] = []
    for tupla in array:

        if valor[0] == tupla[0] and valor[1] == tupla[1]:
            tuplas.append(tupla)

    return tuplas

def search_greedy(lastNo, heuristicas, array: list[tuple[int, int, int]]):
    path = []
    pos_atual = 0

    while (True):
        arestas_conectadasds_comigo = encontrar_tupla_por_valor(pos_atual, array)

        nos_vizinhos = []
        for tupla in arestas_conectadasds_comigo:
            nos_vizinhos.append(tupla[1])

        heuristicas_nos = []
        for no in nos_vizinhos:
            if no in heuristicas:
                valor = heuristicas[no]

                heuristicas_nos.append((no, valor))

        menor = [heuristicas_nos[0]]

        for valor in heuristicas_nos:
            if valor[1] < menor[0][1]:
                menor[0] = valor

        pos_prev = pos_atual
        pos_atual = menor[0][0]


        path.append(encontrar_tupla_por_subtupla((pos_prev, pos_atual), array))

        if pos_atual == lastNo:
            return path


arestas_com_pesos: list[tuple[int, int, int]] = [(0, 1, 10), (0, 2, 5), (1, 4, 4), (1, 2, 4), (1, 3, 1), (2, 4, 6),
                                                 (4, 5, 1),
                                                 (3, 4, 2), (3, 5, 3)]
heuristicas = {0: 12, 1: 4, 2: 5, 3: 3, 4: 1, 5: 1}
path = search_greedy(5, heuristicas, arestas_com_pesos)

print(path)

## Verifico onde estou
## verifico quais as aresta estão conectada comigo
## verifico quais das aresta tem o menor valor na tabela
## vou para aresta de menor valor
## repitor o passo até chegar na aresta que eu quero
