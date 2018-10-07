# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 16:40:39 2018

@author: nicola.dainese96@gmail.com
"""
def adjacency_matrix_rnd(S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    import networkx as nx
    from networkx.algorithms import bipartite
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
    #print('dir_name = ', dir_name)
    file_path = dir_name+'/prova.txt'
    ensure_dir(file_path)
    directory = os.path.dirname(file_path)
    os.chdir(directory)
    #connectance IS NOT fixed, but its average <C> is equal to p
    #anyway on 100 realization no significant difference is detected
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
    ax.set_title('Configurazione casuale con C = '+format(p,'.3f'))
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
    os.chdir(directory2)
    return A1

def adjacency_matrix_rnd2(S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    import networkx as nx
    from networkx.algorithms import bipartite
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
    #print('dir_name = ', dir_name)
    #k is the number of non-null elements of the mutualistic matrix
    #in this case p = C in each realization
    k = int(round(S1*S2*p,0))
    G = bipartite.gnmk_random_graph(S1, S2, k)
    #G = bipartite.random_graph(S1, S2, p)
    num_conn = G.number_of_edges()
    if num_conn != k: #this checks out if the number of connections of the random graphs is really k
        print('Problema numero connessioni.') #prints an alert otherwise
        print('# = ', num_conn)
    deg = list(G.degree())
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
       
    if index == 1:    
        plt.style.use('seaborn')
        
        file_path = dir_name+'/prova.txt'
        ensure_dir(file_path)
        directory = os.path.dirname(file_path)
        os.chdir(directory)
        
        fig, [ax1, ax] = plt.subplots(1,2, figsize = (10,4))
        #fig, [ax1, ax] = plt.subplots(1,2)
        ax1.set_title('Interazioni mutualistiche casuali')
        ax1.set_axis_off()
        ax1.set_autoscale_on(True)
        nx.draw_networkx(G, pos = pos, node_color = colors, ax = ax1)
        
        
        
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        ax.set_ylabel('Impollinatori')
        ax.set_xlabel('Piante')
        ax.set_title('Configurazione casuale con C = '+format(p,'.3f'))
        ax.set_autoscale_on(True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.imshow(A1, cmap = 'Greys')
        plt.tight_layout()
        fig.savefig('random_'+format(p,'.2f')+'.png')
        plt.close()

        
    else: 
        
        file_path = dir_name+'/random_matrix/prova.txt'
        ensure_dir(file_path)
        directory = os.path.dirname(file_path)
        os.chdir(directory)
        
        fig = plt.figure()
        ax = fig.add_subplot(111)
        
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        ax.set_title('Matrice random realizzazione {}'.format(index))
        ax.set_xlabel('S2 = {}'.format(S2))
        ax.set_ylabel('S1 = {}'.format(S1))
        ax.imshow(A1, cmap = 'Greys')
        fig.savefig('random_'+format(p,'.2f')+'-'+repr(index)+'.png')
        plt.close()
        
    #else:
    #    O.print_list_csv(deg1, 'deg1_R-'+repr(index), dir_name)
    #    O.print_list_csv(deg2, 'deg2_R-'+repr(index), dir_name)
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    os.chdir(directory2)
    return A1

def adjacency_matrix_nested (S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    #asymmetric nested (for low values of connectances)
    import networkx as nx
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
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
        G = adjust_edges(G, S1, S2, p) #this is where the actual edges are decided in most cases (C < 0.55)
    if p > 0.55:
        G = adjust_edges2(G, S1, S2, p) #this should be usless in all real-connectance cases 
    deg = list(G.degree())
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
        #togliere quando finito
    if index == 0:
        plt.style.use('seaborn')    
        fig, [ax1, ax] = plt.subplots(1,2, figsize = (10,4))
        
        ax1.set_title('Interazioni mutualistiche nidificate')
        ax1.set_axis_off()
        ax1.set_autoscale_on(True)
        nx.draw_networkx(G, pos = pos, node_color = colors, ax=ax1)
        
        
        
        
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        ax.set_ylabel('Impollinatori')
        ax.set_xlabel('Piante')
        ax.set_title('Configurazione nidificata con C = '+format(p,'.3f'))
        ax.set_autoscale_on(True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.tight_layout()
        
        plt.imshow(A1, cmap = 'Greys')
#rimuovere questa parte 
    if index == 1:    
        plt.style.use('seaborn')  
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        ax.set_ylabel('Impollinatori')
        ax.set_xlabel('Piante')
        ax.set_title('Nested I tipo con C = '+format(p,'.3f'))
        ax.set_autoscale_on(True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.tight_layout()
        plt.imshow(A1, cmap = 'Greys')
    if index == 1:
        fig.savefig('nested_'+format(p,'.2f')+'.png')
    if flag == False:
        if index == 1:    
            my.print_tuple2(deg1, 'N_degree1-'+repr(index2), dir_name)
            my.print_tuple2(deg2, 'N_degree2-'+repr(index2), dir_name)
    else:
        O.print_list_csv(deg1, 'deg1_N-'+repr(index), dir_name)
        O.print_list_csv(deg2, 'deg2_N-'+repr(index), dir_name)
    plt.close()
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    os.chdir(directory2)
    return A1

def adjacency_matrix_nested2 (S1 = 10, S2 = 10, p = 0.33, dir_name = 'graph', index = 1, index2 = 1, flag = False):
    #balanced nested
    import networkx as nx
    import matplotlib.pyplot as plt
    import os
    from ensure_dir import ensure_dir
    import my_print as my
    import my_output as O
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
    #this is where the actual edges are decided in most cases (C < 0.55) - different method
        G = adjust_edges1(G, S1, S2, p)
    if p > 0.55:
        G = adjust_edges2(G, S1, S2, p)
    deg = list(G.degree())
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
    #rimettere if index == 1
    if index == 0:    
        plt.style.use('seaborn')
        fig, [ax1, ax] = plt.subplots(1,2, figsize = (10,4))
        ax1.set_title('Interazioni mutualistiche nidificate')
        ax1.set_axis_off()
        ax1.set_autoscale_on(True)
        nx.draw_networkx(G, pos = pos, node_color = colors, ax=ax1)
    
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        ax.set_ylabel('Impollinatori')
        ax.set_xlabel('Piante')
        ax.set_title('Configurazione nidificata con C = '+format(p,'.2f'))
        ax.set_autoscale_on(True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.imshow(A1, cmap = 'Greys')
        plt.tight_layout()
        fig.savefig('nested_'+format(p,'.2f')+'_II.png')
        
        
    if index == 1:    
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.grid()
        xtics = [x-0.5 for x in range(0,S2+1)]
        ytics = [x-0.5 for x in range(0,S1+1)]
        ax.set_yticks(ytics)
        ax.set_xticks(xtics)
        ax.set_ylabel('Impollinatori')
        ax.set_xlabel('Piante')
        ax.set_title('Nested II tipo con C = '+format(p,'.3f'))
        ax.set_autoscale_on(True)
        plt.setp(ax.get_xticklabels(), visible=False)
        plt.setp(ax.get_yticklabels(), visible=False)
        plt.tight_layout()
        plt.imshow(A1, cmap = 'Greys')
        
    if index == 1:
        fig.savefig('nested_'+format(p,'.2f')+'_II.png')
    if flag == False:
        if index == 1:    
            my.print_tuple2(deg1, 'N_degree1-'+repr(index2), dir_name)
            my.print_tuple2(deg2, 'N_degree2-'+repr(index2), dir_name)
    else:
        O.print_list_csv(deg1, 'deg1_N-'+repr(index), dir_name)
        O.print_list_csv(deg2, 'deg2_N-'+repr(index), dir_name)
    plt.close()
    file_path2 = "C:/Users/Utente/Anaconda3/UserScripts/Programmi cooperazione/"
    directory2 = os.path.dirname(file_path2)
    os.chdir(directory2)
    return A1

def adjust_edges(G, S1, S2, C): #first method of adjusting edges - asymmetric for low Cs
    import networkx as nx
    in_edges = G.number_of_edges()
    #print(in_edges)
    fin_edges = int(round(C*S1*S2,0)) #number of final edges to be obtained
    #print(fin_edges)
    delta = in_edges - fin_edges #final < initial
    #print(delta)
    edges = list(G.edges())
    #print(edges)
    index = []
    for i in range(len(edges)):
    #we start with a triangular matrix [1/0] 
    #edges with lower values will be the first ones to be recided
    #untill the request connectance is achieved
        i_x_i = edges[i][0]*(edges[i][1]-S1) #this is the algorithm that assign a value to each edge
        index.append(i_x_i)
    #print(index)
    M = max(index)
    sort_edg = []
    for i in range(0,M+1):
        for j in range(len(edges)):
            if index[j] == i:
                sort_edg.append(edges[j]) #this list contains the edges ordered with increasing values
    #print(sort_edg)
    new_edges = sort_edg[:-delta]
    F = nx.Graph()
    nodes = [x for x in range(S1+S2)]
    F.add_nodes_from(nodes)
    F.add_edges_from(new_edges)
    return F

def adjust_edges1(G, S1, S2, C): #second method of adjusting edges - more balanced
    import networkx as nx
    in_edges = G.number_of_edges()
    #print('in edges = ', in_edges, '\n')
    fin_edges = int(round(C*S1*S2,0))
    #print('fin_edges = ', fin_edges, '\n')
    delta = in_edges - fin_edges 
    #print('delta = ', delta, '\n')
    edges = list(G.edges())
    #print('edges = ', edges, '\n')
    index = []
    for i in range(len(edges)):
        if i == 0:
            i_x_i = (edges[i][0]+2)*(edges[i][1]-S1+2)
        else:
            i_x_i = (edges[i][0]+1)*(edges[i][1]-S1+1)
        index.append(i_x_i)
    #print('index = ', index, '\n')
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

def adjust_edges2(G, S1, S2, C):
    #import networkx as nx
    Sq = S1*S2
    conn = check_connectance (G, Sq)
    while conn < C:
        for i in range(S1):
            if conn > C:
                break
            deg = G.degree(i)
            if deg < S2:
                G.add_edge(i,deg+S1)
                conn = check_connectance(G, Sq)
            else: 
                continue
      
    return G
    
def check_connectance (G, Sq):
    #import networkx as nx
    in_edges = G.number_of_edges()
    C = in_edges/(Sq)
    return C
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    