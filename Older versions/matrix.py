# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 12:46:04 2018

@author: Utente
"""

def adjacency_matrix_rnd(S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    import networkx as nx
    from networkx.algorithms import bipartite
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
    curr_dir = os.getcwd()
    #print('dir_name = ', dir_name)
    file_path = dir_name+'/prova.txt'
    ensure_dir(file_path)
    directory = os.path.dirname(file_path)
    os.chdir(directory)
    
    G = bipartite.random_graph(S1, S2, p)
    deg = list(G.degree())
    deg1 = deg[:S1]
    deg2 = deg[S1:]
    
    pos = {x:[0,x] for x in range(S1)}
    for j in range(S2):
        pos[S1+j] = [1,j]
    colors = ['r' for i in range(0,S1)]
    for j in range(S2):
        colors.append('b')
    fig, [ax1, ax] = plt.subplots(1,2, figsize = (9,4))
    ax1.set_title('Interazioni mutualistiche casuali')
    ax1.set_axis_off()
    ax1.set_autoscale_on(True)
    nx.draw_networkx(G, pos = pos, node_color = colors, ax = ax1)
    
    A = nx.to_numpy_matrix(G)
    A2 = A.getA()
    A1 = []
    for x in range(S1):
        A1.append(A2[x][S1:])
    
    ax.grid()
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    ax.set_ylabel('Impollinatori')
    ax.set_xlabel('Piante')
    ax.set_title('Configurazione casuale con C = '+format(p,'.2f'))
    ax.set_autoscale_on(True)
    
    plt.imshow(A1, cmap = 'Greys')
    if index == 1:
        fig.savefig('random_'+format(p,'.2f')+'.png')
    plt.close()
    if flag == False:
        if index == 1:
            my.print_tuple2(deg1, 'R_degree1-'+repr(index2), dir_name)
            my.print_tuple2(deg2, 'R_degree2-'+repr(index2), dir_name)
    else:
        O.print_list_csv(deg1, 'deg1_R-'+repr(index), dir_name)
        O.print_list_csv(deg2, 'deg2_R-'+repr(index), dir_name)
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    print('directory2 = ', directory2)
    print('curr_dir = ', curr_dir)
    os.chdir(directory2)
    return A1


def adjacency_matrix_nested (S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    import networkx as nx
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
    curr_dir = os.getcwd()
    file_path = dir_name+'/prova.txt'
    ensure_dir(file_path)
    directory = os.path.dirname(file_path)
    os.chdir(directory)
    #attenzione, funziona bene solo con S1 = S2
    G = nx.Graph()
    nodes = [x for x in range(S1+S2)]
    G.add_nodes_from(nodes)
    #print(list(G.nodes()))
    edges = []
    for i in range(S1):
        for j in range(S1, S1+S2-i):
            edges.append((i,j))
    G.add_edges_from(edges)
    if p < 0.55:
        G = adjust_edges(G, S1, S2, p)
    deg = list(G.degree())
    deg1 = deg[:S1]
    deg2 = deg[S1:]
    pos = {x:[0,x] for x in range(S1)}
    for j in range(S2):
        pos[S1+j] = [1,j]
    colors = ['r' for i in range(0,S1)]
    for j in range(S2):
        colors.append('b')
        
    fig, [ax1, ax] = plt.subplots(1,2, figsize = (9,4))
    ax1.set_title('Interazioni mutualistiche nested ')
    ax1.set_axis_off()
    ax1.set_autoscale_on(True)
    nx.draw_networkx(G, pos = pos, node_color = colors, ax=ax1)
    
    
    A = nx.to_numpy_matrix(G)
    A2 = A.getA()
    A1 = []
    for x in range(S1):
        A1.append(A2[x][S1:])
    
    ax.grid()
    xtics = [x-0.5 for x in range(0,S2+1)]
    ytics = [x-0.5 for x in range(0,S1+1)]
    ax.set_yticks(ytics)
    ax.set_xticks(xtics)
    ax.set_ylabel('Impollinatori')
    ax.set_xlabel('Piante')
    ax.set_title('Configurazione nested  con C = '+format(p,'.2f'))
    ax.set_autoscale_on(True)
    
    plt.imshow(A1, cmap = 'Greys')
    if index == 1:
        fig.savefig('nested_'+format(p,'.2f')+'.png')
    if flag == False:
        if index == 1:    
            my.print_tuple2(deg1, 'N_degree1-'+repr(index2), dir_name)
            my.print_tuple2(deg2, 'N_degree2-'+repr(index2), dir_name)
    else:
        my.print_tuple2(deg1, 'deg1_N-'+repr(index), dir_name)
        my.print_tuple2(deg2, 'deg2_N-'+repr(index), dir_name)
    plt.close()
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    print('directory2 = ', directory2)
    print('curr_dir = ', curr_dir)
    os.chdir(directory2)
    return A1

def adjust_edges(G, S1, S2, C):
    import networkx as nx
    in_edges = G.number_of_edges()
    #print(in_edges)
    fin_edges = int(round(C*S1*S2,0))
    #print(fin_edges)
    delta = in_edges - fin_edges 
    #print(delta)
    edges = list(G.edges())
    #print(edges)
    index = []
    for i in range(len(edges)):
        i_x_i = edges[i][0]*(edges[i][1]-S1)
        index.append(i_x_i)
    #print(index)
    M = max(index)
    sort_edg = []
    for i in range(0,M+1):
        for j in range(len(edges)):
            if index[j] == i:
                sort_edg.append(edges[j])
    #print(sort_edg)
    new_edges = sort_edg[:-delta]
    F = nx.Graph()
    nodes = [x for x in range(S1+S2)]
    F.add_nodes_from(nodes)
    F.add_edges_from(new_edges)
    return F