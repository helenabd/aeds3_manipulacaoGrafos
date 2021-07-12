def recebe_dados (nome):
    #Receber os dados
    arquivo = open(nome, 'r')

    #Recebe o cabeçalho com numero de vertices e arestas
    linha = arquivo.readline()
    listaVA = linha.split(' ')
    num_vertice = int(listaVA[0])
    num_aresta = int(listaVA[1])

    #Cria a lista e a matriz com os dados do arquivo
    listaAdj = [[] for i in range(num_vertice)]
    matAdj = [[0 for i in range(num_vertice)] for i in range(num_vertice)]
    vertice = [i for i in range(num_vertice)]
    aresta = []
    for j in range(num_aresta):
        linha = arquivo.readline()
        linha = linha.split(' ')
        origem = int(linha[0])
        destino = int(linha[1])
        peso = int(linha[2])
        listaAdj[origem].append((destino, peso))
        listaAdj[destino].append((origem, peso))
        matAdj[origem][destino] = peso
        matAdj[destino][origem] = peso
        aresta.append((origem, destino, peso))

    #print(listaAdj)
    #print(matAdj)
    #print(vertice)
    #print(aresta)
    arquivo.close()

    return listaAdj, matAdj, num_vertice, num_aresta


def representacao(listaAd, matrizAd, isMatriz):
    if isMatriz == 1:
        print(matrizAd)
    else:
        print(listaAd)

def informacoes(listaAdj, vertices, arestas):
    vMaior = listaAdj[0]
    vMenor = listaAdj[0]
    maior = 0
    menor = 99999
    for i in range(vertices):
        if listaAdj[i] != []:
            aux = len(listaAdj[i])
            if aux > maior:
                maior = aux
                vMaior = i
            if aux < menor:
                menor = aux
                vMenor = i
    grauMedio = (arestas * 2) / vertices
    print(f"Maior grau: {maior} - vertice:  {vMaior}")
    print(f"Menor grau: {menor} - vertice:  {vMenor}")
    print(f"Grau médio : {grauMedio}")


    # verificar em cada posição da matriz ou lista
        # maior
        # menor
        # grau médio
        # frequencia relativa
#def busca_largura_matriz(grafo, vertice_inicial):
    #salvar em um arquivo de cada linha o vértice e seu nível na árvore de busca
#def busca_largura_lista(listaAdj, vertice_inicial):
    #salvar em um arquivo de cada linha o vértice e seu nível na árvore de busca
#def busca_profundidade_matriz(grafo, vertice_inicial):
    #salvar em um arquivo de cada linha o vértice e seu nível na árvore de busca
def busca_profundidade_lista(G, s):
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in G[u]:
            aux = i[0]
            if desc[aux] == 0:
                desempilhar = False
                S.append(aux)
                R.append(aux)
                desc[aux] = 1
                break
            if desempilhar:
                S.pop()
    print(R)
def busca_profundidade_rec_lista(G, s, marca):
    comp[s] = marca
    for v in G[s]:
        aux = v[0]
        if comp[aux] == 0:
            busca_profundidade_rec_lista(G, aux, marca)
#def componentes_conexos_matriz(grafo):
    #descobrir a quantidade de componentes conexos e a quatidade de vértices de cada um deles
def componentes_conexos_lista(G):
    global comp
    comp = [0 for i in range(len(G))]
    marca = 0
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec_lista(G, u, marca)
    #Quantidade de componentes conexas = marca

    aux = 1
    print(comp)

#if __name__ == 'Trabalho':

#nome = input("Digite o nome do arquivo: ")

#Entrada de dados

dados = recebe_dados('teste.txt')
lista = dados[0]
matriz = dados[1]
vertice = dados[2]
aresta = dados[3]
#isMatriz = int(input("Tipo de Representação: \n1- Matriz \n2-Lista de Adjacencia: "))
#representacao(lista, matriz, isMatriz)
informacoes(lista, vertice, aresta)
busca_profundidade_lista(lista, 0)
componentes_conexos_lista(lista)


