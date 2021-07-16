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
        return matAdj
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

def informacoes_lista(G, vertices, arestas):
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

def informacoes_matriz(G, vertices, arestas):
    #Informações matriz
    cont = 0
    while(cont == 0):
        for i in range(vertices):
            for j in range(vertices):
                if G[i][j] != 0:
                    vMaior = G[i][j]
                    vMenor = G[i][j]
                    cont += 1
    maior = 0
    menor = 99999
    grau = []
    for i in range(vertices):
        aux = 0
        for j in range(vertices):
            if G[i][j] != 0:
                aux += 1
        if aux > maior:
            maior = aux
            vMaior = i
        if aux < menor:
            menor = aux
            vMenor = i
        grau.append(aux)
    grauMedio = (arestas * 2) / vertices
    print(f"Maior grau: {maior} - vertice:  {vMaior}")
    print(f"Menor grau: {menor} - vertice:  {vMenor}")
    print(f"Grau médio : {grauMedio}")
    print(f"Frequencia relativa: ")
    for n in range(menor, (maior+1)):
        print(f"Grau {n}: {grau.count(n)/vertices}")
def busca_largura_matriz(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for v in range(len(G[u])):
            if G[u][v] != 0 and desc[v] == 0:
                Q.append(v)
                R.append(v)
                desc[v] = 1
                nivel[v] = nivel[u] + 1
    #print(R)
    print("Busca largura: ")
    for j in range(len(G)):
        if (nivel[j] != None):
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_largura_matriz.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if (nivel[j] != None):
            arquivo.write(f"{j}: {nivel[j]}\n")

def busca_largura_lista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    Q = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(Q) != 0:
        u = Q.pop(0)
        for v in G[u]:
            aux = v[0]
            if desc[aux] == 0:
                Q.append(aux)
                R.append(aux)
                desc[aux] = 1
                nivel[aux] = nivel[u] + 1
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

def busca_profundidade_matriz(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                desempilhar = False
                S.append(i)
                R.append(i)
                desc[i] = 1
                nivel[i] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()
    #print(R)
    print("Busca por profundidade:")
    for j in range(len(G)):
        if (nivel[j] != None):
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_profundidade_matriz.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if (nivel[j] != None):
            arquivo.write(f"{j}: {nivel[j]}\n")

def busca_profundidade_lista(G, s):
    desc = [0 for i in range(len(G))]
    nivel = [None] * len(G)
    S = [s]
    R = [s]
    desc[s] = 1
    nivel[s] = 0
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
                nivel[aux] = nivel[u] + 1
                break
        if desempilhar:
            S.pop()
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

def busca_profundidade_rec_lista(G, s, marca):
    comp[s] = marca
    for v in G[s]:
        aux = v[0]
        if comp[aux] == 0:
            busca_profundidade_rec_lista(G, aux, marca)

def busca_profundidade_rec_matriz(G, s, marca):
    comp[s] = marca
    for v in range(len(G[s])):
        if G[s][v] != 0 and comp[v] == 0:
            busca_profundidade_rec_matriz(G, v, marca)

def componentes_conexos_lista(G):
    global comp
    comp = [0 for i in range(len(G))]
    marca = 0
    n = 0
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec_lista(G, u, marca)
    #Quantidade de componentes conexas = marca
    #Varredura da lista de componentes para separação dos grupos
    n = max(comp)
    print(f"Componentes conexas : {marca}")
    for j in range(1,(n+1)):
        print(f"{j}: {comp.count(j)} vertices")
    #print(comp)

def componentes_conexos_matriz(G):
    global comp
    comp = [0 for i in range(len(G))]
    marca = 0
    n = 0
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_rec_matriz(G, u, marca)
    #Quantidade de componentes conexas = marca
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
"""informacoes_lista(G, vertice, aresta)
busca_profundidade_lista(G, 0)"""
busca_largura_lista(G, 0)
#componentes_conexos_lista(G)
#informacoes_matriz(G, vertice, aresta)
#busca_largura_matriz(G, 0)
#busca_profundidade_matriz(G, 0)
#componentes_conexos_matriz(G)


