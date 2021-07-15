def recebe_dados (nome):
    #Receber os dados

    #Recebe o cabeçalho com numero de vertiarquivo = open(nome, 'r')
    arquivo = open(nome, 'r')
    linha = arquivo.readline()
    listaVA = linha.split(' ')
    num_vertice = int(listaVA[0])
    num_aresta = int(listaVA[1])
    G = representacao(2, arquivo, num_vertice, num_aresta)

    vertice = [i for i in range(num_vertice)]
    aresta = []
    """for j in range(num_aresta):
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
        aresta.append((destino, origem, peso))"""

    #print(listaAdj)
    #print(matAdj)
    #print(vertice)
    #print(aresta)
    arquivo.close()

    return num_vertice, num_aresta, G


def representacao(isMatriz, arquivo, num_vertice, num_aresta):
    if isMatriz == 1:
        matAdj = [[0 for i in range(num_vertice)] for i in range(num_vertice)]
        for j in range(num_aresta):
            linha = arquivo.readline()
            linha = linha.split(' ')
            origem = int(linha[0])
            destino = int(linha[1])
            peso = int(linha[2])
            matAdj[origem][destino] = peso
            matAdj[destino][origem] = peso
            #aresta.append((origem, destino, peso))
            #aresta.append((destino, origem, peso))
        return matrizAd
    else:
        listaAdj = [[] for i in range(num_vertice)]
        for j in range(num_aresta):
            linha = arquivo.readline()
            linha = linha.split(' ')
            origem = int(linha[0])
            destino = int(linha[1])
            peso = int(linha[2])
            listaAdj[origem].append((destino, peso))
            listaAdj[destino].append((origem, peso))
            #aresta.append((origem, destino, peso))
            #aresta.append((destino, origem, peso))
        return listaAdj

def informacoes(G, vertices, arestas):
    #Informações lista
    vMaior = G[0]
    vMenor = G[0]
    maior = 0
    menor = 99999
    grau = []
    for i in range(vertices):
        if G[i] != []:
            aux = len(G[i])
            grau.append(aux)
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
    print(f"Frequencia relativa: ")
    for n in range(menor, (maior+1)):
        print(f"Grau {n}: {grau.count(n)/vertices}")


#def busca_largura_matriz(grafo, vertice_inicial):
    #salvar em um arquivo de cada linha o vértice e seu nível na árvore de busca
def busca_largura_lista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    marcado = [False] * len(G)
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    marcado[s] = True
    while len(Q) != 0:
        u = Q.pop(0)
        for v in G[u]:
            aux = v[0]
            if desc[aux] == 0:
                Q.append(aux)
                R.append(aux)
                desc[aux] = 1
                if (not marcado[aux]):
                    nivel[aux] = nivel[u] + 1
                    marcado[aux] = True
    # print(R)
    print("Busca largura: ")
    for j in range(len(G)):
        if (nivel[j] != None):
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_largura_lista.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if (nivel[j] != None):
            arquivo.write(f"{j}: {nivel[j]}\n")

#def busca_profundidade_matriz(grafo, vertice_inicial):
    #salvar em um arquivo de cada linha o vértice e seu nível na árvore de busca
def busca_profundidade_lista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    marcado = [False] * len(G)
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    marcado[s] = True
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
                if (not marcado[aux]):
                    nivel[aux] = nivel[u] + 1
                    marcado[aux] = True
                break
            if desempilhar:
                S.pop()
<<<<<<< HEAD
    print(R)
=======
    #print(R)
    print("Busca por profundidade:")
    for j in range(len(G)):
        if (nivel[j] != None):
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_profundidade_lista.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if (nivel[j] != None):
            arquivo.write(f"{j}: {nivel[j]}\n")
>>>>>>> 596ae473d9416fe4a051a595463dddabec6b7a9d

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
    n = 0
    #número de componentes conexas
    comp_con = 0
    # lista de quantos grupos conexos têm
    rastreio_comp_con=[]
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec_lista(G, u, marca)
    #Quantidade de componentes conexas = marca
    pos_comp = comp[0]
    #Varredura da lista de componentes para separação dos grupos
    n = max(comp)
    print(f"Componentes conexas : {marca}")
    for j in range(1,(n+1)):
        print(f"{j}: {comp.count(j)} vertices")
    #print(comp)


#if __name__ == 'Trabalho':

#nome = input("Digite o nome do arquivo: ")

#Entrada de dados
dados = recebe_dados('teste.txt')
vertice = dados[0]
aresta = dados[1]
G = dados[2]
#isMatriz = int(input("Tipo de Representação: \n1- Matriz \n2-Lista de Adjacencia: "))
informacoes(G, vertice, aresta)
busca_profundidade_lista(G, 0)
<<<<<<< HEAD
=======
busca_largura_lista(G, 0)
>>>>>>> 596ae473d9416fe4a051a595463dddabec6b7a9d
componentes_conexos_lista(G)


