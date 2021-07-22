def recebe_dados(nome, rep):
    arquivo = open(nome, 'r')
    linha = arquivo.readline()
    listaVA = linha.split(' ')
    num_vertice = int(listaVA[0])
    num_aresta = int(listaVA[1])
    G = representacao(rep, arquivo, num_vertice, num_aresta)

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
        return listaAdj


def informacoes_lista(G, vertices, arestas):
    # Informações lista
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
    for n in range(menor, (maior + 1)):
        print(f"Grau {n}: {grau.count(n) / vertices}")


def informacoes_matriz(G, vertices, arestas):
    # Informações matriz
    cont = 0
    while cont == 0:
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
    for n in range(menor, (maior + 1)):
        print(f"Grau {n}: {grau.count(n) / vertices}")


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
    # print(R)
    print("Busca largura: ")
    for j in range(len(G)):
        if nivel[j] is not None:
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_largura_matriz.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if nivel[j] is not None:
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
        if nivel[j] is not None:
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_largura_lista.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if nivel[j] is not None:
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
    # print(R)
    print("Busca por profundidade:")
    for j in range(len(G)):
        if nivel[j] is not None:
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_profundidade_matriz.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if nivel[j] is not None:
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
    # print(R)
    print("Busca por profundidade:")
    for j in range(len(G)):
        if nivel[j] is not None:
            print(f"{j}: {nivel[j]}")
    arquivo = open('busca_profundidade_lista.txt', 'w')
    arquivo.write("vertice:nivel\n")
    for j in range(len(G)):
        if nivel[j] is not None:
            arquivo.write(f"{j}: {nivel[j]}\n")


def busca_profundidade_comp_conexa_lista(G, s, marca):
    comp[s] = marca
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
        comp[u] = marca
        if desempilhar:
            S.pop()


def busca_profundidade_comp_conexa_matriz(G, s, marca):
    comp[s] = marca
    desc = [0 for i in range(len(G))]
    S = [s]
    R = [s]
    desc[s] = 1
    while len(S) != 0:
        u = S[-1]
        desempilhar = True
        for i in range(len(G[u])):
            if G[u][i] != 0 and desc[i] == 0:
                desempilhar = False
                S.append(i)
                R.append(i)
                desc[i] = 1
                break
        comp[u] = marca
        if desempilhar:
            S.pop()


def componentes_conexos_lista(G):
    global comp
    comp = [0 for i in range(len(G))]
    marca = 0
    n = 0
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_comp_conexa_lista(G, u, marca)
    n = max(comp)
    print(f"Componentes conexas : {marca}")
    for j in range(1, (n + 1)):
        print(f"{j}: {comp.count(j)} vertices")
    # print(comp)


def componentes_conexos_matriz(G):
    global comp
    comp = [0 for i in range(len(G))]
    marca = 0
    n = 0
    for u in range(len(G)):
        if comp[u] == 0:
            marca += 1
            busca_profundidade_comp_conexa_matriz(G, u, marca)
    n = max(comp)
    print(f"Componentes conexas : {marca}")
    for j in range(1, (n + 1)):
        print(f"{j}: {comp.count(j)} vertices")
    # print(comp)


# -----------------------------------------------------------------------#

# MENU

nome = input("Digite o nome do arquivo: ")
rep = int(input("Tipo de Representação: \n1. Matriz \n2. Lista de Adjacencia: "))
while (rep != 1 and rep != 2):
    print("Opção inválida")
    rep = int(input("Tipo de Representação: \n1. Matriz \n2. Lista de Adjacencia: "))

# Entrada de dados
dados = recebe_dados(nome, rep)
vertice = dados[0]
aresta = dados[1]
G = dados[2]

# Menu de opções para o usuário
ans = True
if (rep == 1):
    while (ans):
        print("""
        1. Informações
        2. Busca por Largura
        3. Busca por Profundidade
        4. Componentes Conexos
        5. Sair
        """)
        op = int(input("Qual operação deseja realizar? "))
        if (op == 1):
            informacoes_matriz(G, vertice, aresta)
        elif (op == 2):
            v = int(input("Informe o vértice de partida: "))
            busca_largura_matriz(G, v)
        elif (op == 3):
            v = int(input("Informe o vértice de partida: "))
            busca_profundidade_matriz(G, v)
        elif (op == 4):
            componentes_conexos_matriz(G)
        elif (op == 5):
            ans = False
elif rep == 2:
    while ans:
        print("""
        1. Informações
        2. Busca por Largura
        3. Busca por Profundidade
        4. Componentes Conexos
        5. Sair
        """)
        op = int(input("Qual operação deseja realizar? "))
        if op == 1:
            informacoes_lista(G, vertice, aresta)
        elif op == 2:
            v = int(input("Informe o vértice de partida: "))
            busca_largura_lista(G, v)
        elif op == 3:
            v = int(input("Informe o vértice de partida: "))
            busca_profundidade_lista(G, v)
        elif op == 4:
            componentes_conexos_lista(G)
        elif (op == 5):
            ans = False
