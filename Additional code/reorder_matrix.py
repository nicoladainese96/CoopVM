# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 17:59:50 2018

@author: Utente
"""

def ordina_grafo_1(G, S1, S2):
    import networkx as nx
    deg = list(G.degree())
    deg1 = deg[:S1]
    deg2 = deg[S1:]
    #print('deg1 = ', deg1, '\n')
    #print('deg2 = ', deg2, '\n')
    #print('deg primo vertice = ', G.degree(0), '\n')
    
    vdeg1 = []
    for i in range(len(deg1)):
        vdeg1.append(G.degree(i))
    #print('vdeg1 = ', vdeg1, '\n')
    
    M1 = max(vdeg1)
    #print('massimo grado vertici primo gruppo = ', M1, '\n')
    
    index1 = []
    for i in range(M1 + 1):
        for j in range(len(vdeg1)):
            if i == vdeg1[j]:
                index1.append(j)
    #print('vertici in ordine crescente di grado: ', index1, '\n')
    
    index1.reverse() 
    #print('vertici in ordine decrescente di grado: ', index1, '\n')
    
    edges = G.edges()
    #print('lista dei legami tra due vertici: ', edges, '\n')
    
    G1 = nx.Graph()
    nodes = [x for x in range(S1+S2)]
    G1.add_nodes_from(nodes)
    #print('nodi nuovo grafo: ', G1.nodes(), '\n')
    
    for i in range(len(index1)):
        for T in edges:
            if T[0] == index1[i]:
                G1.add_edge(i, T[1])
                
    new_vdeg1 = []
    for i in range(len(deg1)):
        new_vdeg1.append(G1.degree(i))
    #print('new_vdeg1 = ', new_vdeg1, '\n')
    
    return G1

def ordina_grafo_2(G, S1, S2):
    import networkx as nx
    deg = list(G.degree())
    deg1 = deg[:S1]
    deg2 = deg[S1:]
    print('deg1 = ', deg1, '\n')
    print('deg2 = ', deg2, '\n')
    print('deg primo vertice secondo gruppo = ', G.degree(S1), '\n')
    
    vdeg2 = []
    for i in range(len(deg2)):
        vdeg2.append(G.degree(S1+i))
    print('vdeg2 = ', vdeg2, '\n')
    
    M2 = max(vdeg2)
    print('massimo grado vertici secondo gruppo = ', M2, '\n')
    
    index2 = []
    for i in range(M2 + 1):
        for j in range(len(vdeg2)):
            if i == vdeg2[j]:
                index2.append(j)
    print('vertici in ordine crescente di grado: ', index2, '\n')
    
    index2.reverse() 
    print('vertici in ordine decrescente di grado: ', index2, '\n')
    
    edges = G.edges()
    print('lista dei legami tra due vertici: ', edges, '\n')
    
    G1 = nx.Graph()
    nodes = [x for x in range(S1+S2)]
    G1.add_nodes_from(nodes)
    print('nodi nuovo grafo: ', G1.nodes(), '\n')
    
    for i in range(len(index2)):
        for T in edges:
            if T[1] == index2[i] + S1:
                G1.add_edge(T[0], i+S1)
                
    new_edges = G1.edges()
    print('lista dei legami tra due vertici: ', new_edges, '\n')       
    
    new_vdeg2 = []
    for i in range(len(deg2)):
        new_vdeg2.append(G1.degree(S1+i))
    print('new_vdeg2 = ', new_vdeg2, '\n')
    
    return G1

def adjacency_matrix_rnd(S1 = 10, S2 = 10, p = 0.35, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    import networkx as nx
    from networkx.algorithms import bipartite
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
    from grad_nestedness import NODF_calc
    plt.style.use('seaborn')
    curr_dir = os.getcwd()
    #print('dir_name = ', dir_name)
    file_path = dir_name+'/prova.txt'
    ensure_dir(file_path)
    directory = os.path.dirname(file_path)
    os.chdir(directory)
    k = int(p*S1*S2)
    G = bipartite.gnmk_random_graph(S1, S2, k)
    G1 = ordina_grafo_1(G, S1, S2)
    G1 = ordina_grafo_2(G1, S1, S2)
    
    deg = list(G1.degree())
    deg1 = deg[:S1]
    deg2 = deg[S1:]
    pos = {x:[0,x] for x in range(S1)}
    for j in range(S2):
        pos[S1+j] = [1,j]
    colors = ['r' for i in range(0,S1)]
    for j in range(S2):
        colors.append('b')
        
    A = nx.to_numpy_matrix(G)
    A2 = A.getA()
    A1 = []
    for x in range(S1):
        A1.append(A2[x][S1:])
        
    NODF = NODF_calc(A1)
    print('NODF prima del riordino = ', NODF, '\n')
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    ax.set_ylabel('Impollinatori')
    ax.set_xlabel('Piante')
    ax.set_title('Configurazione casuale con C = '+format(p,'.2f'))
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.imshow(A1, cmap = 'Greys')
    plt.tight_layout()
    
    fig.savefig('random_'+format(p,'.2f')+'.png')
    plt.close()
    
    A = nx.to_numpy_matrix(G1)
    A2 = A.getA()
    A1 = []
    for x in range(S1):
        A1.append(A2[x][S1:])
        
    #NODF = NODF_calc(A1)
    #print('NODF dopo il riordino = ', NODF, '\n')
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111)
    #ax.grid()
    #xtics = [x-0.5 for x in range(0,S2+1)]
    #ytics = [x-0.5 for x in range(0,S1+1)]
    #ax.set_yticks(ytics)
    #ax.set_xticks(xtics)
    #ax.set_ylabel('Impollinatori')
    #ax.set_xlabel('Piante')
    #ax.set_title('Configurazione casuale con C = '+format(p,'.2f'))
    #plt.setp(ax.get_xticklabels(), visible=False)
    #plt.setp(ax.get_yticklabels(), visible=False)
    #plt.imshow(A1, cmap = 'Greys')
    #plt.tight_layout()
    
    #fig.savefig('random_'+format(p,'.2f')+'_ordinata.png')
    #plt.close()
       
    fig, [ax1, ax] = plt.subplots(1,2, figsize = (10,4))
    ax1.set_title('Interazioni mutualistiche casuali')
    ax1.set_axis_off()
    ax1.set_autoscale_on(True)
    nx.draw_networkx(G1, pos = pos, node_color = colors, ax=ax1)

    ax.grid()
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    ax.set_ylabel('Impollinatori')
    ax.set_xlabel('Piante')
    ax.set_title('Configurazione casuale con C = '+format(p,'.2f'))
    ax.set_autoscale_on(True)
    plt.setp(ax.get_xticklabels(), visible=False)
    plt.setp(ax.get_yticklabels(), visible=False)
    plt.imshow(A1, cmap = 'Greys')
    plt.tight_layout()
    
    fig.savefig('random_'+format(p,'.2f')+'_ordinata.png')
    plt.close()    
    
    print('curr_dir = ', curr_dir)
    os.chdir(curr_dir)
    return A1

adjacency_matrix_rnd(dir_name = "C:/Users/Utente/Anaconda3/Cooperazione/matrici")
from bipartite_graph_matrix import adjacency_matrix_nested2
adjacency_matrix_nested2(p = 0.35, dir_name = "C:/Users/Utente/Anaconda3/Cooperazione/matrici", index = 0 )