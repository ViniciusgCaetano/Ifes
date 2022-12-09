import streamlit as st
def discover_path(graph):
    n = len(graph)
    numofadj = []
 
    # Pegar número de ajacências
    for i in range(n):
        numofadj.append(sum(graph[i]))
 
    # Descobrir quantos vértices ímpares existem, e se existir, pegar ele como ponto
    # inicial para a resolução 
    startpoint, numofodd = 0, 0
    for i in range(n - 1, -1, -1):
        if (numofadj[i] % 2 == 1):
            numofodd += 1
            startpoint = i

    # inicializar variáveis
    stack = []
    path = []
    cur = startpoint
 
    # Procurar até encontrar um vértice que possua vizinho
    while (len(stack) > 0 or sum(graph[cur])!= 0):
         
        # Caso esse vértice não possua vizinhos, será adicionado ao caminho
        if (sum(graph[cur]) == 0):
            path.append(cur)
            cur = stack[-1]
            del stack[-1]
 
        # Caso possua algum vizinho, o vértice será adicionado a pilha
        # Deletar vértice entre os dois
        else:
            for i in range(n):
                if (graph[cur][i] == 1):
                    stack.append(cur)
                    graph[cur][i] = 0
                    graph[i][cur] = 0
                    cur = i
                    break
 
    # Mostrar caminho
    final_str = ''
    for ele in path:
        final_str += f'A{ele+1} -> '
        
    final_str += f'A{cur+1}'
    st.header(final_str)